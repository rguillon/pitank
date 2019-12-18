import yaml
try:
        from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
        from yaml import Loader, Dumper

from MicroWebSrv2  import *
from config import conf
from tasks import tasks

@WebRoute(GET, '/light1', name='light1')
def RequestTestPost(microWebSrv2, request) :

    dimmer_conf = yaml.dump(conf.get_conf('dimmer1'), Dumper = Dumper)

    print(dimmer_conf)

    content = """\
        <!DOCTYPE html>
        <html>
            <head>
                <title>Light 1</title>
                <link rel="stylesheet" href="style.css" />
            </head>
            <body>
                <h2>Light 1</h2>
                
                <br />
                <form action="/light1" method="post">
                    Dimmer Table  i
                    <br/>
                    <textarea name="conf" rows="16" cols="32">%s</textarea>
                    <br/>
                    <input type="submit" value="Update">
                </form>
           </body>
        </html>
    """ % dimmer_conf
    request.Response.ReturnOk(content)

#                    Dimmer Table  <input type="text" name="table" value="%s" style="font-size: 18pt; height: 1240px; width:600px; "><br />


@WebRoute(POST, '/light1', name='light1 update')
def RequestTestPost(microWebSrv2, request) :
    data = request.GetPostedURLEncodedForm()
    try :
        new_conf = yaml.load(data['conf'], Loader = Loader)
        tasks.get_task('dimmer1').update_conf(new_conf)
        #if the update_conf did not raise any exception, thn the conf if valid, save it
        conf.set_conf('dimmer1', new_conf)
        conf.save_conf()
    except Exception as e:
        print(e)
        request.Response.ReturnBadRequest()
        return
    request.Response.ReturnRedirectGet('/light1')

    
    

def config_mws():
    # All pages not found will be redirected to the home '/',
    mws2.SetEmbeddedConfig()
    mws2.NotFoundURL = '/'

# Instanciates the MicroWebSrv2 class,
mws2 = MicroWebSrv2()


