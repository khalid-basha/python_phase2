import time
def timeit(fun):
    def wrapper(*args, **kw):
        start_time = time.time()
        result = fun(*args, **kw)
        end_time = time.time()
        print ('func:%r args:[%r, %r] took: %2.6f sec' % \
          (fun.__name__, args, kw, end_time-start_time))
        return result
    return wrapper

def login_required(fun):
    def wrapper(*args, **kwargs):
        #suppose we have a list of sessions here
        if args[0] in session or kwargs['username'] in session:
            return fun(*args, **kwargs)
        else:
            print("You are not pass!")
            return #redirect function(*args,**kwargs) to log in page or something like that
    return wrapper

@app.route('/webhook/order/paid', methods=['POST'])
@timeit
@login_required
def paid_order_webhook(username,password):
    order_event = json.loads(request.data.decode('utf-8'))
    OrderComponent.handle_paid_order_event(order_event=order_event)
    return 'Success', 200
