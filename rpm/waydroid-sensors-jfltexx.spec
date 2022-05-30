Name:           waydroid-sensors-jfltexx
Version:        1.0.0
Release:        1
Summary:        Waydroid-sensors-jfltexx installs the waydroid-sensord for the Galaxy S4 (jfltexx).
License:        GPLv3
URL:            https://github.com/edp17/waydroid-sensors-jfltexx
BuildArch:      %{arm}
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  systemd
Requires:       waydroid
Requires:       waydroid-jfltexx

%description
Waydroid uses Linux namespaces (user, pid, uts, net, mount, ipc) to run a full Android system in a container and provide Android applications on any GNU/Linux-based platform.

The Android system inside the container has direct access to any needed hardware.

The Android runtime environment ships with a minimal customized Android system image based on LineageOS. The image is currently based on Android 10.

Waydroid-sensors-jfltexx installs the waydroid-sensord for the Galaxy S4 (jfltexx).

%prep
%setup

%install
mkdir -p %{buildroot}/usr/local/bin

install -D -m644 config/waydroid-sensord %{buildroot}/usr/local/bin/waydroid-sensord

%clean
rm -rf $RPM_BUILD_ROOT

%post
systemctl daemon-reload
systemctl-user daemon-reload
systemctl-user start waydroid-sensors
chmod +x /usr/local/bin/waydroid-sensord

%files
%defattr(-,root,root,-)
/usr/lib/systemd/user/waydroid-sensors.service
/usr/local/bin/waydroid-sensord
