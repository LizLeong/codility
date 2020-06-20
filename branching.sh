git tag
git checkout v2.6.4
git switch -c rapiscan
git status
git checkout -b release/v2.7.0 rapiscan
git status
git checkout -b feature/bitbucket_integration release/v2.7.0
git add .gitmodules
git commit -m "use bitbucket instead of github"
# does git push put it on branch feature/bitbucket_integration

# do I push to origin? I want it to go into just the feature branch, is origin release/v2.7.0 instead?
git push --set-upstream origin feature/bitbucket_integration

# XXX: the new feature is inside feature branch feature/bb_integrate ....doesn't look right, it's from origin.
# now merge it to the release branch
git checkout release/v2.7.0
git merge feature/bitbucket_integration

# now tag this as rc1
git tag -a "v2.7.0-rc1" -m "v2.7.0-rc1 bitbucket integration"
git push origin --tags

# create own feature branchs and proceed as above
# add new logo
# add new config files

# when all is good, tag the final release/v2.7.0 with v2.7.0 tag
git checkout release/v2.7.0
git tag -a "v2.7.0" -m "v2.7.0 released"
git push origin --tags

# CONFIRM THIS: merge this back into rapiscan branch
git checkout rapiscan
git merge release/v2.7.0
git push --set-upstream origin  rapiscan

# next time you release, take it from rapiscan branch

