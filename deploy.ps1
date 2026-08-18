# deploy.ps1 — publish a delivered site bundle to muend.github.io
#
# Usage, from anywhere:
#   .\deploy.ps1                                  # uses the newest muend-site-*.zip in Downloads
#   .\deploy.ps1 -Zip C:\path\to\muend-site.zip   # or point at one explicitly
#   .\deploy.ps1 -Message "Custom commit message"
#
# Run it from inside the repo working copy. It extracts the bundle over the repo,
# shows you what changed, asks once, then commits and pushes.

param(
  [string]$Zip = "",
  [string]$Message = "Update site",
  [switch]$Yes            # skip the confirmation prompt
)

$ErrorActionPreference = "Stop"

# --- sanity: are we in the repo? -------------------------------------------
if (-not (Test-Path ".git")) {
  Write-Host "This does not look like the repo root (no .git folder here)." -ForegroundColor Red
  Write-Host "cd into your muend.github.io working copy and run it again." -ForegroundColor Red
  exit 1
}

# --- find the bundle --------------------------------------------------------
if (-not $Zip) {
  $candidate = Get-ChildItem "$HOME\Downloads\muend-site*.zip" -ErrorAction SilentlyContinue |
               Sort-Object LastWriteTime -Descending | Select-Object -First 1
  if (-not $candidate) {
    Write-Host "No muend-site*.zip found in Downloads. Pass one with -Zip." -ForegroundColor Red
    exit 1
  }
  $Zip = $candidate.FullName
}
if (-not (Test-Path $Zip)) { Write-Host "Not found: $Zip" -ForegroundColor Red; exit 1 }
Write-Host "Bundle: $Zip" -ForegroundColor Cyan

# --- commit identity: GitHub rejects pushes that expose a private address ----
$email = git config user.email
if (-not $email -or $email -notmatch "users\.noreply\.github\.com") {
  Write-Host "Setting commit identity to your GitHub noreply address." -ForegroundColor Yellow
  git config user.name  "muend"
  git config user.email "173892601+muend@users.noreply.github.com"
}

# --- get up to date, then extract over the working copy ---------------------
git pull --ff-only origin main
Expand-Archive -Path $Zip -DestinationPath . -Force

if (-not (Test-Path ".gitignore")) {
  "__pycache__/`n*.pyc`n.DS_Store" | Set-Content -Encoding utf8 .gitignore
}

# --- show the damage before doing anything irreversible ---------------------
git add -A
$changes = git status --short
if (-not $changes) { Write-Host "Nothing changed. Already up to date." -ForegroundColor Green; exit 0 }

Write-Host ""
Write-Host "Changes to be committed:" -ForegroundColor Cyan
$changes | ForEach-Object { Write-Host "  $_" }

$deleted = $changes | Where-Object { $_ -match '^D' }
if ($deleted) {
  Write-Host ""
  Write-Host "WARNING: the bundle does not contain these tracked files, so they" -ForegroundColor Yellow
  Write-Host "would be deleted. Check this is what you want." -ForegroundColor Yellow
}

if (-not $Yes) {
  Write-Host ""
  $reply = Read-Host "Commit and push to main? (y/N)"
  if ($reply -ne "y") { Write-Host "Stopped. Nothing was pushed." -ForegroundColor Yellow; exit 0 }
}

# --- ship -------------------------------------------------------------------
git commit -m $Message
git push origin main

Write-Host ""
Write-Host "Pushed. GitHub Pages usually publishes within a minute or two." -ForegroundColor Green
Write-Host "  https://muend.github.io          (English)"
Write-Host "  https://muend.github.io/tr/      (Turkish)"
Write-Host "Open with Ctrl+Shift+R to bypass the browser cache." -ForegroundColor Gray
