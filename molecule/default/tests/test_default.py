import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


PACKAGE = "stacer"
PACKAGE_BINARY = "/usr/bin/stacer"


def test_stacer_package_installed(host):
    """
    Tests if stacer package is installed.
    """
    assert host.package(PACKAGE).is_installed


def test_stacer_binary_exists(host):
    """
    Tests if stacer binary file exists.
    """
    assert host.file(PACKAGE_BINARY).exists


def test_stacer_binary_file(host):
    """
    Tests if stacer binary is a file type.
    """
    assert host.file(PACKAGE_BINARY).is_file


def test_stacer_binary_which(host):
    """
    Tests the output to confirm stacer's binary location.
    """
    assert host.check_output('which stacer') == PACKAGE_BINARY
