@echo off
cd /d "C:\Path\To\Your\Repo"
git pull origin main
git commit --allow-empty -m "keep alive"
git push origin main
