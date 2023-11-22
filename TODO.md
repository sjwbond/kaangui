## Web Client

userid hardcoded
backend url hardcoded

clean up spreadsheet component
improve undo performance
better error handling
clean up code and refactor
unit tests

## Desktop Client

do profiling and speed up loading of models and saving of properties table
update unit tests
  gui\uis\custom\api.py
  gui\uis\windows\open_model\open_model.py
  gui\uis\windows\screens
  gui\uis\windows\screens2
  results page

## Ideas

if someone puts an urgent task, it should be approved, maybe add a note
alternative idea: urgent is 99 and simon's is 100

on insertion of duplicate job if job hasn't started, update priority, otherwise wait
caveat: what if they were created by different people?

add job cancellation

Job Management:
- List of jobs sorted by execution order (priority)
- Create/delete/modify job
- Change job priority
- Cancel running job
- Start job right now/push job to front of queue
- Show job run time
- Show job history
