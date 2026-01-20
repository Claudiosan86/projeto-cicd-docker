# Projeto CI/CD - Automação Docker Hub

![CI/CD Pipeline](https://github.com/Claudiosan86/projeto-cicd-docker/actions/workflows/pipeline.yml/badge.svg)

## Descrição
Este projeto demonstra a implementação de uma esteira de **CI/CD (Integração e Entrega Contínua)** utilizando GitHub Actions e Docker.

### Tecnologias Utilizadas
* **Linguagem:** Python
* **Container:** Docker
* **Automação:** GitHub Actions
* **Registry:** Docker Hub

### Fluxo de Trabalho
1. O desenvolvedor realiza o `push` do código para a branch `main`.
2. O **GitHub Actions** dispara automaticamente o workflow.
3. É realizado o login seguro no **Docker Hub** via Secrets.
4. A imagem Docker é construída e enviada para o repositório público `claudiosanroman/projeto-cicd-python`.

### Como executar
Para baixar a imagem gerada por este projeto:
```bash
docker pull claudiosanroman/projeto-cicd-python:latest
