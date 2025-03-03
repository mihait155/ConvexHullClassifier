from repository.Repo import *
from service.Service import *
from ui.UI import *

if __name__ == '__main__':
    repo = Repo()
    service = Service(repo)
    ui = UI(service)
    ui.run()

