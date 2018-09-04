import constants
from .exceptions import InvalidPropertyException
from .exceptions import InvalidIDException
from .exceptions import MandatoryPropertyException


def all_fields_mandatory(props):
    return valid_properties(constants.ALL_TOPOLOGY_PROPS, constants.ALL_TOPOLOGY_PROPS, props)


def topology_mandatory_fields_set(props):
    return valid_properties(constants.ALL_TOPOLOGY_PROPS, constants.MANDATORY_TOPOLOGY_PROPS, props)


def valid_controller_properties(props):
    return valid_properties(constants.ALL_CONTROLLER_PROPS, constants.MANDATORY_CONTROLLER_PROPS, props)


def valid_controller_id_property(props):
    return valid_id_prop(constants.ID_CONTROLLER_PROPS, props)


def valid_host_properties(props):
    return valid_properties(constants.ALL_HOST_PROPS, constants.MANDATORY_HOST_PROPS, props)


def valid_host_id_property(props):
    return valid_id_prop(constants.ID_HOST_PROPS, props)


def valid_switch_properties(props):
    return valid_properties(constants.ALL_SWITCH_PROPS, constants.MANDATORY_SWITCH_PROPS, props)


def valid_switch_id_property(props):
    return valid_id_prop(constants.ID_SWITCH_PROPS, props)


def valid_link_properties(props):
    return valid_properties(constants.ALL_LINK_PROPS, constants.MANDATORY_LINK_PROPS, props)


def valid_link_id_property(props):
    return valid_id_prop(constants.ID_LINK_PROPS, props)


def valid_interface_properties(props):
    return valid_properties(constants.ALL_INTERFACE_PROPS, constants.MANDATORY_INTERFACE_PROPS, props)


def valid_interface_id_property(props):
    return valid_id_prop(constants.ID_INTERFACE_PROPS, props)


def valid_customer_properties(props):
    return valid_properties(constants.ALL_CUSTOMER_PROPS, constants.MANDATORY_CUSTOMER_PROPS, props)


def valid_customer_id_property(props):
    return valid_id_prop(constants.ID_CUSTOMER_PROPS, props)


def valid_properties(all_props, mandatory_props, props):
    invalid_props = set(props).difference(all_props)
    missing_props = mandatory_props.difference(props)
    if invalid_props:
        raise InvalidPropertyException(invalid_props=invalid_props)
    elif missing_props:
        raise MandatoryPropertyException(mandatory_props=missing_props)
    return True


def valid_id_prop(id_props, props):
    if (id_props.difference(props)) > 2:
        return True
    else:
        raise InvalidIDException(invalid_ids=props)
