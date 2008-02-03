#
Summary:	An Objective-C framework for regular expressions
Name:		RegexKit
Version:	0.6.0
Release:	0.1
License:	BSD
Group:		Applications
Source0:	http://dl.sourceforge.net/regexkit/%{name}_%{version}_source.tar.bz2
# Source0-md5:	75118aec7b4879efe148c0772e834919
Patch0:		%{name}-Linux.patch
URL:		http://regexkit.sourceforge.net/
BuildRequires:	gnustep-base-devel >= 1.13.0
BuildRequires:	pcre-devel >= 7.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
RegexKit is an Objective-C framework for regular expressions.

%package devel
Summary:	Header files for RegexKit library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki RegexKit
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	pcre-devel >= 7.6

%description devel
Header files for RegexKit library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki RegexKit.

%prep
%setup -q -n %{name}_%{version}_source
%patch0 -p1

%build
export GNUSTEP_MAKEFILES=%{_datadir}/GNUstep/Makefiles
export GNUSTEP_FLATTENED=yes
cd GNUstep
%{__make} \
	messages=yes

#%{__make} \
#	CFLAGS="%{rpmcflags}" \
#	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
export GNUSTEP_MAKEFILES=%{_datadir}/GNUstep/Makefiles
export GNUSTEP_FLATTENED=yes
rm -rf $RPM_BUILD_ROOT

cd GNUstep
%{__make} install \
	messages=yes \
	GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
	DESTDIR=$RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_libdir}/libRegexKit.so.0.0.1

%files devel
%defattr(644,root,root,755)
%dir %{_includedir}/RegexKit
%{_includedir}/RegexKit/*.h
%{_libdir}/libRegexKit.so
