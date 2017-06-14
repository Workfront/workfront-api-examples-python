from api import StreamClient, ObjCode, AtTaskObject

def example():
    client = StreamClient('http://localhost:8080/attask/api')
    print 'Logging in...'
    client.login('admin','user')
    print 'Done'

    print 'Retrieving user...'
    user = AtTaskObject(client.get(ObjCode.USER,client.user_id,['ID','homeGroupID','emailAddr']))
    print 'Done'
    print user

    print 'Searching projects...'
    results = client.search(ObjCode.PROJECT,{'groupID':user.homeGroupID})
    print 'Done'

    print '%s project(s) found' % len(results)
    for p in results:
        project = AtTaskObject(p)
        print ' - %s' % project.name

    print 'Creating project...'
    project = AtTaskObject(client.post(ObjCode.PROJECT,{'name':'My Project','groupID':user.homeGroupID}))
    print 'Done'
    print project

    print 'Retrieving project...'
    project = AtTaskObject(client.get(ObjCode.PROJECT,project.ID))
    print 'Done'
    print project

    print 'Editing project...'
    project = AtTaskObject(client.put(ObjCode.PROJECT,project.ID,{'ownerID':user.ID}),client)
    print 'Done'
    print project

    print 'Deleting project...'
    client.delete(ObjCode.PROJECT,project.ID)
    print 'Done'

    print 'Creating another project...'
    project = AtTaskObject({},client)
    project.objCode = ObjCode.PROJECT
    project.name = 'My New Project'
    project.groupID = user.homeGroupID
    project.save()
    print 'Done'
    print project

    print 'Editing another project...'
    project.ownerID = user.ID
    project.save()
    print 'Done'
    print project

    print 'Deleting another project...'
    client.delete(ObjCode.PROJECT,project.ID)
    print 'Done'

    print 'Logging out...'
    client.logout()
    print 'Done'
    
if __name__ == '__main__':
    example()
