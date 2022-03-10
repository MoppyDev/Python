from ldap3 import Tls
import ssl
from flask_ldap3_login import LDAP3LoginManager
 
def ldap_authentication(user_name, user_pwd):
 
    config = dict()

    config['LDAP_HOST'] = 'ENTER LDAP HOST HERE i.e, ldaps://domain.com'

    # Port number of your LDAP server
    config['LDAP_PORT'] = 636

    # Base DN of your directory
    config['LDAP_BASE_DN'] = 'ENTER BASE DN HERE i.e, {DC=domain,DC=com}'

    # Users DN to be prepended to the Base DN
    config['LDAP_USER_DN'] = 'cn=users'

    # Groups DN to be prepended to the Base DN
    config['LDAP_GROUP_DN'] = 'CN=Users'

    # Specify the server connection should use SSL
    config['LDAP_USE_SSL'] = True

    # Instruct Flask-LDAP3-Login to not automatically add the server
    config['LDAP_ADD_SERVER'] = False

    ldap_manager = LDAP3LoginManager()
    ldap_manager.init_config(config)

    # Configure certificates for TLS connectivity
    tls_ctx = Tls(
    validate=ssl.CERT_NONE,
    version=ssl.PROTOCOL_TLSv1_2,
    ca_certs_file='',
    valid_names=[
        '*',
        ]
    )
    
    ldap_manager.add_server(
        config.get('LDAP_HOST'),
        config.get('LDAP_PORT'),
        config.get('LDAP_USE_SSL'),
        tls_ctx=tls_ctx
    )
    response = ldap_manager.authenticate_direct_credentials(user_name, user_pwd)
    if 'success' in str(response.status):
        l_success_msg = True
    else:
        l_success_msg = False
 
    return l_success_msg