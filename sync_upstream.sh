git fetch upstream
git merge upstream/master
git checkout team-edit
git add .
git commit -m "SyncWithUpstream"
git push origin team-edit