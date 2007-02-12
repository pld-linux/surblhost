# TODO
# - resolv linking failure? checking for res_init in -lresolv... no
#
Summary:	Check if hostnames are blacklisted by surbl.org
Summary(pl.UTF-8):	Sprawdzanie czy hosty są na czarnej liście surbl.org
Name:		surblhost
Version:	0.6.0
Release:	1
License:	GPL v2
Group:		Applications
Source0:	http://dl.sourceforge.net/surblhost/%{name}-%{version}.tar.bz2
# Source0-md5:	59a3d610906b19bb19bfa336734902c0
URL:		http://surblhost.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Surblhost is a small program to see if hostnames are listed in the
Spam URI Realtime Blocklists (SURBL).

%description -l pl.UTF-8
Surblhost to mały program do sprawdzania, czy hosty są na czarnej
liście SURBL (Spam URI Realtime Blocklists).

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/surblhost
%{_mandir}/man1/surblhost.1*
