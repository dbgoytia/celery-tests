
## Celery tests

It's a project to test queueing systems in Python. 

You can checkout the celery tutorial followed here: https://docs.celeryproject.org/en/stable/getting-started/introduction.html


To start of the project, initailize the backend:

```
docker run -d -p 6379:6379 redis
```

Then initialize the message broker
```
docker run -d -p 5672:5672 rabbitmq
```

Initialize the queue
```
celery -A proj worker -l INFO
```

You will see the queue running something like this:

```
celery -A proj worker -l INFO


celery@EPMXGUAW0888 v5.0.5 (singularity)

macOS-10.16-x86_64-i386-64bit 2021-11-05 11:38:12

[config]
.> app:         proj:0x7ff592863ee0
.> transport:   amqp://guest:**@localhost:5672//
.> results:     redis://localhost/
.> concurrency: 8 (prefork)
.> task events: OFF (enable -E to monitor tasks in this worker)

[queues]
.> celery           exchange=celery(direct) key=celery


[tasks]
  . proj.tasks.add
  . proj.tasks.mul
  . proj.tasks.xsum

[2021-11-05 11:38:13,298: INFO/MainProcess] Connected to amqp://guest:**@127.0.0.1:5672//
[2021-11-05 11:38:13,315: INFO/MainProcess] mingle: searching for neighbors
[2021-11-05 11:38:14,371: INFO/MainProcess] mingle: all alone
[2021-11-05 11:38:14,415: INFO/MainProcess] celery@EPMXGUAW0888 ready.
```

---

## Running tasks in the queue

Execute the following python script to test some of the things that you can do.
Of course, take into consdieration that this is meant to be **asynchronous**

```
python add.py
```
