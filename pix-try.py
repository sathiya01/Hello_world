#gh api \
#  --method POST \
#  -H "Accept: application/vnd.github+json" \
#  /repos/OWNER/REPO/releases \
#  -f tag_name='v1.0.0' \
# -f target_commitish='master' \
# -f name='v1.0.0' \
# -f body='Description of the release' \
# -F draft=false \
# -F prerelease=false \
# -F generate_release_notes=false

import requests
import os, sys
import fileinput
import re
import subprocess

latest_tag = ''
project_url = 'https://api.github.com/repos/sathiya01/Hello_world/releases/latest'
#"https://api.github.com/repos/{owner}/{repo}/releases/latest"

def fetchLatestTag():
  response = requests.get(project_url)
  global latest_tag
  latest_tag = response.json()


def gitPublishRelease(version, releaseNotes,releaseTitle):
#    gh release create v2.2.1 --notes "bugfix release"
#FIXME: pass draft
    cmd = "gh release create %s --notes '%s' --title '%s'"%(version,releaseNotes, releaseTitle)
    print(cmd)

    os.system(cmd)

if __name__ == "__main__":
  fetchLatestTag()
  gitPublishRelease('v2.0.2','release note new check','release title')
