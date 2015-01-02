RPM Spec for Consul-UI
======================

To Build
---------

To build the RPM (non-root user):

1. Check out this repo
2. Install rpmdevtools and mock 

    ```
    sudo yum install rpmdevtools mock
    ```
3. Set up your rpmbuild directory tree

    ```
    rpmdev-setuptree
    ```
4. Link the spec file and sources from the repository into your rpmbuild/SOURCES directory

    ```
    ln -s ${repo}/SPECS/consul-ui.spec rpmbuild/SPECS/
    ln -s ${repo}/SOURCES/* rpmbuild/SOURCES/
    ```
5. Download remote source files

    ```
    spectool -g -R rpmbuild/SPECS/consul-ui.spec
    ```
6. Build the RPM

    ```
    rpmbuild -ba rpmbuild/SPECS/consul-ui.spec
    ```

More info
---------
See the [consul.io](http://www.consul.io) website.
