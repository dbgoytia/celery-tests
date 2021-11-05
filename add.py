from proj.tasks import add
from proj.celery import app

result = add.delay(2,2)

print(result.ready())                 # Wether the task has finished executing 
print(result.get(timeout=1))          # Wait for the task to complete, rarely used because you want it to be asynchronous
print(result.get(propagate=False))    # Get results
print(result.traceback)               # See traceback in case there's any issues with the task


# You can get more granularity using apply_async()
add.apply_async((2, 2))

result = add.apply_async((2, 2), queue='lopri', countdown=10) # Execute task in a queue named lo-pri, 10 secs after message is sent

print(result.id)

res = app.AsyncResult(result.id)
print(res.state)
