# PyZn

This is the repository for the backend service, if you want to check the frontend check this repo https://github.com/khulnasoft/pyzn-front

## 💖 Sponsors

<!-- sponsors --><a href="https://github.com/samuelcolvin"><img src="https:&#x2F;&#x2F;avatars.githubusercontent.com&#x2F;u&#x2F;4039449?u&#x3D;42eb3b833047c8c4b4f647a031eaef148c16d93f&amp;v&#x3D;4" width="60px" alt="Samuel Colvin" /></a><a href="https://github.com/sethmlarson"><img src="https:&#x2F;&#x2F;avatars.githubusercontent.com&#x2F;u&#x2F;18519037?u&#x3D;41090cc65ae0a34aee49c7a35cfbd40e2e12eb53&amp;v&#x3D;4" width="60px" alt="Seth Michael Larson" /></a><a href="https://github.com/pavdmyt"><img src="https:&#x2F;&#x2F;avatars.githubusercontent.com&#x2F;u&#x2F;10200820?u&#x3D;a470afb0d60b966be8b046d78f3a4401cbce0987&amp;v&#x3D;4" width="60px" alt="Pavel Dmytrenko" /></a><a href="https://github.com/SermetPekin"><img src="https:&#x2F;&#x2F;avatars.githubusercontent.com&#x2F;u&#x2F;96650846?u&#x3D;441ab17ab6c7b1c0690e755d46d33b0259b498f5&amp;v&#x3D;4" width="60px" alt="Sermet Pekin" /></a><!-- sponsors -->

## ⚒️ Start contributing
I wanted to make the setup of the environment as easy as possible. To start the environment you need the 
following prerequisites:

### Prerequisites
  * bash (+4.3)
  * docker (+17.05)
  * docker-compose (+1.16.1)
  * docker-py (+2.2.1)
  * ansible (+2.3)
  
### Start environment
You only (_fingers crossed_) need to execute the following to start the environment:

```commandline
make start-containers
```

## Architecture and patterns
Principally I used some DDD concepts (like value objects, entities, and so on) and also CQS whose objective is to
separate commands from queries.

The structure of the code is the following:
  * `pyzn/application`: here is where all the commands and the queries are located.
  * `pyzn/domain`: domain objects like entities, exceptions, and value objects.
  * `pyzn/infrastructure`: infrastructure components like the implementation of the repository
    class like DB or BigQuery, the Flask web application, the container, and so on.
    * `pyzn/infrastructure/cli`: the command line programs.
    * `pyzn/infrastructure/container`: config files and the dependency injection manager.
    * `pyzn/infrastructure/api`: the api endpoints controller.
    
## FAQ
**Where the downloads come from?**

The data is retrieved from the official BigQuery repository: https://packaging.python.org/guides/analyzing-pypi-package-downloads/

**When the data is updated?**

There is a cron that runs every day at 5 pm UTC that retrieves all the new downloads from the previous day.

## 🚩 License
The code is available under the [MIT license](LICENSE.md).
