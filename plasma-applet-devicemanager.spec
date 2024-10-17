%define		oname  devicemanager
Summary:	Device manager that shows the not removable devices too
Name:		plasma-applet-%oname
Version: 	1.1.1
Release: 	%mkrel 1
Source0:	106051-%oname-%version.tar.bz2
License: 	GPLv2+
Group: 		Graphical desktop/KDE
Url: 		https://kde-look.org/content/show.php/Device+Manager?content=106051
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	plasma-devel


%description 
This is the Device Notifier with two changes:
- It shows the not removable devices too
- When there are more than one action for a device instead of opening 
  that ugly window it adds one button per action under the device
- Margin in the left of the actions to distinguish them from the devices
- Option to automount devices
- Option that makes the dialog hide after some time after the 
  insertion of a removable device

%files
%defattr(-,root,root)
%{_kde_libdir}/kde4/*
%{_kde_datadir}/kde4/services/*


%prep
%setup -q -n %oname


%build
%cmake_kde4
%make


%install
rm -rf %{buildroot}
cd build
%{makeinstall_std}
cd -


%clean
rm -rf %{buildroot}
