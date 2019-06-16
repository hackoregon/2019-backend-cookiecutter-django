#! /bin/bash

set -e

# Tag, Push and Deploy only if it's not a pull request
if [ -z "$TRAVIS_PULL_REQUEST" ] || [ "$TRAVIS_PULL_REQUEST" == "false" ]; then

    # Push only if we're testing the master branch
    #if [ "$TRAVIS_BRANCH" == "master" ]; then

    # Deploy only if this is a tag push
    if [ -n "$TRAVIS_TAG" ]; then

        echo Getting the ECR login...
        eval $(aws ecr get-login --no-include-email --region $AWS_DEFAULT_REGION)

        REMOTE_DOCKER_PATH="$DOCKER_REPO"/"$DOCKER_REPO_NAMESPACE"/"$DOCKER_IMAGE"
        
        # tag with branch and travis build number then push
        TAG=travis-buildnum-"$TRAVIS_BUILD_NUMBER"
        echo Tagging with "$TAG"
        docker tag "$DOCKER_IMAGE":latest "$REMOTE_DOCKER_PATH":"$TAG"    
        docker push "$REMOTE_DOCKER_PATH":"$TAG"

        # tag with "latest" then push
        TAG=latest
        echo Tagging with "$TAG"
        docker tag "$DOCKER_IMAGE":latest "$REMOTE_DOCKER_PATH":"$TAG"
        docker push "$REMOTE_DOCKER_PATH":"$TAG"
        
        #echo Running ecs-deploy.sh script...
        bin/ecs-deploy.sh  \
           --service-name "$ECS_SERVICE_NAME" \
           --cluster "$ECS_CLUSTER"   \
           --image "$REMOTE_DOCKER_PATH":latest \
           --timeout 300
    else
        #echo "Skipping deploy because branch is not master"
        echo "Skipping deploy because tag is not set"
    fi
else
    echo "Skipping deploy because it's a pull request"
fi