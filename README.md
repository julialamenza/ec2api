# ec2api
Rest Api dentro de um docker que cria instâncias no aws e passa informaços da mesma.

Voce precisará buildar o docker 

docker build -t ece2api .

depois executar o container 
passando as credenciais do seu usuário no aws

docker run -d --name ctnr_ec2api -e AWS_ACCESS_KEY_ID=seu_acess_key -e AWS_SECRET_ACCESS_KEY=seu_secret_acess_key -p 8080:8080 ec2api

Depois disso rodar o programa
python api.py

ai você terá como acessar a api pelo 0.0.0.0:8080/create
onde virá um form para você preencher com os dados da sua instância

em 0.0.0.0:8080/api/info/sua_region -> onde você precisará colcoar o nome da região onde suas instâncias foram criadas lhe retornará as informações delas. (em breve terá um front mais bonitinho para isso)
