#!/usr/bin/env bash
# awscli_s3: AWS CLI S3 upload/download helper.
set -euo pipefail

usage() {
  cat <<USAGE
Usage:
  $0 upload <local_path> <s3://bucket/key>
  $0 download <s3://bucket/key> <local_path>

Environment:
  AWS_PROFILE   Optional named profile (defaults to env credentials)
  AWS_REGION    Optional region override
USAGE
}

require_cmd() {
  command -v "$1" >/dev/null 2>&1 || { echo "Missing dependency: $1" >&2; exit 1; }
}

[ $# -lt 3 ] && { usage; exit 1; }
action=$1
source_path=$2
dest_path=$3

require_cmd aws

aws_args=()
[ -n "${AWS_PROFILE:-}" ] && aws_args+=("--profile" "$AWS_PROFILE")
[ -n "${AWS_REGION:-}" ] && aws_args+=("--region" "$AWS_REGION")

case "$action" in
  upload)
    aws "${aws_args[@]}" s3 cp "$source_path" "$dest_path" --recursive
    ;;
  download)
    aws "${aws_args[@]}" s3 cp "$source_path" "$dest_path" --recursive
    ;;
  *)
    usage
    exit 1
    ;;
esac

echo "Completed $action between $source_path and $dest_path"
