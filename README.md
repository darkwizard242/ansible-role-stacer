[![build-test](https://github.com/darkwizard242/ansible-role-stacer/workflows/build-and-test/badge.svg?branch=master)](https://github.com/darkwizard242/ansible-role-stacer/actions?query=workflow%3Abuild-and-test) [![release](https://github.com/darkwizard242/ansible-role-stacer/workflows/release/badge.svg)](https://github.com/darkwizard242/ansible-role-stacer/actions?query=workflow%3Arelease) ![Ansible Role](https://img.shields.io/ansible/role/51595?color=dark%20green%20) ![Ansible Role](https://img.shields.io/ansible/role/d/51595?label=role%20downloads) ![Ansible Quality Score](https://img.shields.io/ansible/quality/51595?label=ansible%20quality%20score) [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-stacer&metric=alert_status)](https://sonarcloud.io/dashboard?id=ansible-role-stacer) [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-stacer&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=ansible-role-stacer) [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-stacer&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=ansible-role-stacer) [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-stacer&metric=security_rating)](https://sonarcloud.io/dashboard?id=ansible-role-stacer) ![GitHub tag (latest SemVer)](https://img.shields.io/github/tag/darkwizard242/ansible-role-stacer?label=release) ![GitHub repo size](https://img.shields.io/github/repo-size/darkwizard242/ansible-role-stacer?color=orange&style=flat-square)

# Ansible Role: stacer

Role to install (_by default_) [stacer](https://oguzhaninan.github.io/Stacer-Web/#features) or uninstall (_if passed as var_) on **Ubuntu** systems.

## Requirements

None.

## Role Variables

Available variables are listed below (located in `defaults/main.yml`):

### Variables list:

```yaml
stacer_app: stacer
stacer_app_desired_state: present
stacer_ubuntu_repo: 'ppa:oguzhaninan/stacer'
stacer_ubuntu_repo_desired_state: present
stacer_ubuntu_repo_filename: stacer
```

### Variables table:

Variable                         | Description
-------------------------------- | -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
stacer_app                       | Defines the app to install i.e. **stacer**
stacer_package_desired_state     | Defined to dynamically chose whether to install (i.e. either `present` or `latest`) or uninstall (i.e. `absent`) the package. Default is set to `present`.
stacer_ubuntu_repo               | Refers to the ppa repo to add. _Applies only to Ubuntu (16.04 and 18.04) systems, not required for Ubuntu 20.04 systems._
stacer_ubuntu_repo_desired_state | Defined to dynamically chose whether to add/keep (i.e. `present`) or remove (i.e. `absent`) the repository file list from `/etc/apt/sources.list.d`. _Applies only to Ubuntu (16.04 and 18.04) systems, not required for Ubuntu 20.04 systems._
stacer_ubuntu_repo_filename      | Defined to set the repository file name for saving in `/etc/apt/sources.list.d`. _Applies only to Ubuntu (16.04 and 18.04) systems, not required for Ubuntu 20.04 systems._

## Dependencies

None

## Example Playbook

For default behaviour of role (i.e. installation of **stacer** package) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.stacer
```

For customizing behavior of role (i.e. installation of latest **stacer** package) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.stacer
  vars:
    stacer_package_desired_state: latest
```

For customizing behavior of role (i.e. un-installation of **stacer** package) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.stacer
  vars:
    stacer_package_desired_state: absent
```

## License

[MIT](https://github.com/darkwizard242/ansible-role-stacer/blob/master/LICENSE)

## Author Information

This role was created by [Ali Muhammad](https://www.alimuhammad.dev/).
