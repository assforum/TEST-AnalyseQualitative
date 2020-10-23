@ECHO OFF
setlocal DISABLEDELAYEDEXPANSION
SET BIN_TARGET=%~dp0/../yooper/php-text-analysis/interactive
bash "%BIN_TARGET%" %*
