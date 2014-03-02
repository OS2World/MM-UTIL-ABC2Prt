Name:      abc2prt
Version:   1.0.2
Release:   1
Summary:   A program to extract parts from multivoice ABC files.
License:   GPL
URL:       http://abcplus.sourceforge.net
Group:     Applications/File
Prefix:    %{_prefix}
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
Source:    http://abcplus.sourceforge.net/%{name}-%{version}.tar.gz

%description
abc2prt is a simple program to extract parts from multivoice ABC music files.

%prep
%setup -q

%build
make CFLAGS="$RPM_OPT_FLAGS -Wall"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/abc2prt
%{_bindir}/install -s -m 755 abc2prt $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf "$RPM_BUILD_ROOT"

%files
%defattr(-,root,root)
%doc COPYING INSTALL README
%{_bindir}/*

