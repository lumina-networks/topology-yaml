import pytest
from topology import api

@pytest.fixture(scope='module')
def mock_topo_props(request):
    return {
        'controllers': [{
            'name': 'test_controller',
            'protocol': 'https',
            'ip': '127.0.0.1',
            'port': 8443,
            'user': 'admin',
            'password': 'admin'
        }],
        'links': [{
            'source': 'switch_1',
            'destination': 'switch_2'
        }],
        'switches': [{
            'name': 'switch_1',
            'dpid': '123',
            'protocol': 'OpenFlow13'
        },{
            'name': 'switch_2',
            'dpid': '456',
            'protocol': 'OpenFlow13'
        }],
        'customers': [{
            'customer': 'test_customer',
            'connects_to': 'test_endpoint_name',
            'hostname': 'test_host_name',
            'port': 20
        }]
    }


@pytest.fixture(scope='module')
def mock_topo_full(request):
    return {
        'controllers': [{
            'name': 'test_controller',
            'protocol': 'https',
            'ip': '127.0.0.1',
            'port': 8443,
            'user': 'admin',
            'password': 'admin'
        }],
        'hosts': [],
        'links': [{
            'source': 'switch_1',
            'destination': 'switch_2'
        }],
        'switches': [{
            'name': 'switch_1',
            'dpid': '123',
            'protocol': 'OpenFlow13'
        },{
            'name': 'switch_2',
            'dpid': '456',
            'protocol': 'OpenFlow13'
        }],
        'interfaces': [],
        'customers': [{
            'customer': 'test_customer',
            'connects_to': 'test_endpoint_name',
            'hostname': 'test_host_name',
            'port': 20
        }]
    }


@pytest.fixture(scope='module')
def mock_topo_content(request):
    return '''controllers:
- ip: 127.0.0.1
  name: test_controller
  password: admin
  port: 8443
  protocol: https
  user: admin
hosts: []
interfaces: []
links:
- destination: switch_2
  source: switch_1
switches:
- dpid: '123'
  name: switch_1
  protocol: OpenFlow13
- dpid: '456'
  name: switch_2
  protocol: OpenFlow13
customers:
- connects_to: test_endpoint_name
  customer: test_customer
  hostname: test_host_name
  port: 20
'''


def test_create_topology(mock_topo_props, mock_topo_content, tmpdir):
    p = tmpdir.mkdir("sub").join("topo.yml")
    api.create_topology(p.strpath, **mock_topo_props)
    content = p.read()
    assert content == mock_topo_content


def test_read_topology(mock_topo_props, mock_topo_full, tmpdir):
    p = tmpdir.mkdir("sub").join("topo.yml")
    api.create_topology(p.strpath, **mock_topo_props)
    topo = api.read_topology(p.strpath)
    assert topo.__dict__ == mock_topo_full


def test_read_topology(mock_topo_props, mock_topo_full, tmpdir):
    p = tmpdir.mkdir("sub").join("topo.yml")
    api.create_topology(p.strpath, **mock_topo_props)
    topo = api.read_topology(p.strpath)
    assert topo.__dict__ == mock_topo_full
