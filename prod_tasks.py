from invoke import run as invoke_run, task


@task
def prodserver(context, daemon=False, unbuffered=True, host='0.0.0.0', port=8080, workers=2, timeout=3600):
    daemon = ' --daemon' if daemon is True else ''
    unbuffered = 'TRUE' if unbuffered is True else 'FALSE'
    app = 'server:app'
    cmd = f"gunicorn --bind {host}:{port}{daemon} --workers {workers} --timeout {timeout} {app}"
    invoke_run(cmd, env={'PYTHONPATH': './app', 'PYTHONUNBUFFERED': unbuffered})
