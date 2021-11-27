# Run api

    pip install -r requirements.txt,
    python manage.py makemigrations,
	python manage.py migrate
	python3 manage.py runserver 0.0.0.0:7000

# Run api with docker
    docker-compose up -d

## Endpoints

### **Default**

- default (Read the first observation on top of this doc)

|Method|Endpoint        |  Communication  |
|------|----------------|-----------------|   
|`GET` |`/`|    `REST`    |

<br>

<table>
<tr>
<th>Response</th>
</tr>
<tr>
<td>

```json
{
}
```

</td>
</tr>
</table>

### **User**

- registro usuário usando nick único e senha

| Method | Endpoint | Description | BP | QP |
| :---: | :---: | :---: | :---: | :---: |
| GET | `/v1/users` | It returns the details of all user|
| POST | `/v1/users` | It enter new user |

<table>
<tr>
<th>On Success</th>
<th>On Error</th>
</tr>
<tr>
<td>

```json
{
  "name": 'paulo',
  'telefone': '923453925',
  'email': "jhon@gmail.com",
  'password': '1234'
}
status : 201
```

</td>
<td>

```json
{
  False
} status : 404

```

</td>
</tr>
</table>

### **Tweet**

- Tweet (Criação / remoção)
- Like / deslike

| Method | Endpoint | Description | Communication  |
| :---: | :---: | :---: | :---:|
| GET | `/v1/tweets` | It returns the details of all user| `REST` |
| POST | `/v1/tweets` | It post new tweets |`REST`|
| PUT | `/v1/tweets/like` | It Like or dislike |`REST`|

<table>
> Method  POST
<tr>
<th>On Success</th>
<th>On Error</th>
</tr>
<tr>
<td>

```json
{
  "user": "ef5da2dc-3b46-4d30-92f2-154f6f75f1ad",
  "description": "Olá primeiro tweets",
  "midia": "/source/test.png",
  "emoji": "",
  "gif": ""
}

```

</td>
<td>

```json
{
  False
} status : 404

```

</td>
</tr>
</table>

<table>
> Method  PUT
<tr>
<td>

```json
{
  "id": "59b26050-cf1f-4ae6-a017-c95aa7108bc9"
}

```

</td>
<td>

```json
{
  False
} status : 404

```

</td>
</tr>
</table>

### **Retweet**

- Retweet Diferencial
- Like / deslike

| Method | Endpoint | Description | Communication  |
| :---: | :---: | :---: | :---:|
| GET | `/v1/retweets` | It returns the details of all retweets| `REST` |
| POST | `/v1/retweets` | It post retweets |`REST`|
| PUT | `/v1/retweets/like` | It Like or dislike |`REST`|

<table>
> Method  POST
<tr>
<th>On Success</th>
<th>On Error</th>
</tr>
<tr>
<td>

```json
{
  "tweet": "59b26050-cf1f-4ae6-a017-c95aa7108bc9",
  "description": "Olá Retweets"
}

```

</td>
<td>

```json
{
  False
} status : 404

```

</td>
</tr>
</table>

<table>
> Method  PUT
<tr>
<td>

```json
{
  "id": "ef5da2dc-3b46-4d30-92f2-154f6f75f1ad"
}

```

</td>
<td>

```json
{
  False
} status : 404

```

</td>
</tr>
</table>