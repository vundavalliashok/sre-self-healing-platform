.PHONY: test build run k8s-deploy k8s-delete

test:
	cd app && pytest -q

build:
	docker build -f dockerfile -t reliable-api:1.0 .

run:
	docker run --rm -p 8000:8000 reliable-api:1.0

k8s-deploy:
	kubectl apply -f kubernetes/namespace.yaml
	kubectl apply -f kubernetes/serviceaccount.yaml
	kubectl apply -f kubernetes/deployment.yaml
	kubectl apply -f kubernetes/service.yaml
	kubectl apply -f kubernetes/pdb.yaml
	kubectl apply -f kubernetes/hpa.yaml
	kubectl apply -f kubernetes/network-policy.yaml
	kubectl apply -f kubernetes/service-monitor.yaml

k8s-delete:
	kubectl delete namespace sre-platform
