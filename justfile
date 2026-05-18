set windows-shell := ['C:\Windows\System32\cmd.exe', '/c']


# docker compose
doco *args:
	docker compose -p ws_graph -f containers/stack-dev.yml {{args}}

# compose up: Creates and starts docker services
up:
	just doco up -d

down:
	just doco down --remove-orphans