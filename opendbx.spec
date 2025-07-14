#
# Conditional build:
%bcond_without	ibase		# ibase (InterBase/Firebird) backend
%bcond_with	oracle		# oracle backend [BR: libclntsh or liboci + oci.h]
%bcond_without	static_libs	# static library

%ifnarch %{ix86} %{x8664} sparc sparcv9 alpha ppc
%undefine	with_ibase
%endif

Summary:	Extensible library for database access
Summary(pl.UTF-8):	Rozszerzana biblioteka dostępu do baz danych
Name:		opendbx
Version:	1.4.6
Release:	6
License:	LGPL v2+
Group:		Libraries
Source0:	http://linuxnetworks.de/opendbx/download/%{name}-%{version}.tar.gz
# Source0-md5:	3e89d7812ce4a28046bd60d5f969263d
Patch0:		%{name}-tds.patch
Patch1:		doxygen-update.patch
URL:		http://www.linuxnetworks.de/doc/index.php/OpenDBX
%{?with_ibase:BuildRequires:	Firebird-devel}
BuildRequires:	docbook2X
BuildRequires:	libstdc++-devel
BuildRequires:	freetds-devel
BuildRequires:	mysql-devel
BuildRequires:	postgresql-devel
BuildRequires:	sqlite-devel
BuildRequires:	sqlite3-devel
BuildRequires:	unixODBC-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OpenDBX is an extremely lightweight but extensible database access
library written in C. It provides an abstraction layer to all
supported databases with a single, clean and simple interface that
leads to an elegant code design automatically. If you want your
application to support different databases with little effort, this is
definitively the right thing for you!

%description -l pl.UTF-8
OpenDBX to skrajnie lekka, ale rozszerzalna biblioteka dostępu do baz
danych napisana w C. Udostępnia warstwę abstrakcji dla wszystkich
obsługiwanych baz danych w jednym, przejrzystym i prostym interfejsie
automatycznie prowadzącym do eleganckiego projektu kodu. Jest to
odpowiednia biblioteka, aby małym nakładem pracy aplikacja obsługiwała
różne bazy danych.

%package devel
Summary:	Header files for opendbx
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki opendbx
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for opendbx.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki opendbx.

%package static
Summary:	Static opendbx library
Summary(pl.UTF-8):	Statyczna biblioteka opendbx
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static opendbx library.

%description static -l pl.UTF-8
Statyczna biblioteka opendbx.

%package apidocs
Summary:	API documentation for opendbx library
Summary(pl.UTF-8):	Dokumentacja API biblioteki opendbx
Group:		Documentation

%description apidocs
API documentation for opendbx library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki opendbx.

%package backend-firebird
Summary:	Firebird backend for opendbx
Summary(pl.UTF-8):	Backend bazy danych Firebird dla biblioteki opendbx
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description backend-firebird
Firebird backend for opendbx.

%description backend-firebird -l pl.UTF-8
Backend bazy danych Firebird dla biblioteki opendbx.

%package backend-mssql
Summary:	MS SQL backend for opendbx
Summary(pl.UTF-8):	Backend bazy danych MS SQL dla biblioteki opendbx
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description backend-mssql
MS SQL backend for opendbx.

%description backend-mssql -l pl.UTF-8
Backend bazy danych MS SQL dla biblioteki opendbx.

%package backend-mysql
Summary:	MySQL backend for opendbx
Summary(pl.UTF-8):	Backend bazy danych MySQL dla biblioteki opendbx
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description backend-mysql
MySQL backend for opendbx.

%description backend-mysql -l pl.UTF-8
Backend bazy danych MySQL dla biblioteki opendbx.

%package backend-odbc
Summary:	ODBC backend for opendbx
Summary(pl.UTF-8):	Backend baz danych ODBC dla biblioteki opendbx
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description backend-odbc
ODBC backend for opendbx.

%description backend-odbc -l pl.UTF-8
Backend baz danych ODBC dla biblioteki opendbx.

%package backend-oracle
Summary:	Oracle backend for opendbx
Summary(pl.UTF-8):	Backend bazy danych Oracle dla biblioteki opendbx
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description backend-oracle
Oracle backend for opendbx.

%description backend-oracle -l pl.UTF-8
Backend bazy danych Oracle dla biblioteki opendbx.

%package backend-postgres
Summary:	PostgreSQL backend for opendbx
Summary(pl.UTF-8):	Backend bazy danych PostgreSQL dla biblioteki opendbx
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description backend-postgres
PostgreSQL backend for opendbx.

%description backend-postgres -l pl.UTF-8
Backend bazy danych PostgreSQL dla biblioteki opendbx.

%package backend-sqlite3
Summary:	sqlite3 backend for opendbx
Summary(pl.UTF-8):	Backend bazy danych sqlite3 dla biblioteki opendbx
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description backend-sqlite3
sqlite3 backend for opendbx.

%description backend-sqlite3 -l pl.UTF-8
Backend bazy danych sqlite3 dla biblioteki opendbx.

%package backend-sqlite
Summary:	sqlite backend for opendbx
Summary(pl.UTF-8):	Backend bazy danych sqlite dla biblioteki opendbx
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description backend-sqlite
sqlite backend for opendbx.

%description backend-sqlite -l pl.UTF-8
Backend bazy danych sqlite dla biblioteki opendbx.

%package backend-sybase
Summary:	sybase backend for opendbx
Summary(pl.UTF-8):	Backend bazy danych sybase dla biblioteki opendbx
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description backend-sybase
sybase backend for opendbx.

%description backend-sybase -l pl.UTF-8
Backend bazy danych sybase dla biblioteki opendbx.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1

# To fix Doxygen parsing issue
ln -s api lib/%{name}/api.dox

%build
CPPFLAGS="%{rpmcppflags} -I/usr/include/mysql"
%configure \
	%{!?with_static_libs:--disable-static} \
	--with-backends="%{?with_ibase:firebird} mssql mysql odbc %{?with_oracle:oracle} pgsql sqlite sqlite3 sybase"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# opendbx and opendbx-utils domains
%find_lang %{name} --all-name

%{__rm} $RPM_BUILD_ROOT%{_libdir}/%{name}/*.la
%if %{with static_libs}
%{__rm} $RPM_BUILD_ROOT%{_libdir}/%{name}/*.a
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/odbx-sql
%attr(755,root,root) %{_libdir}/libopendbx.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libopendbx.so.1
%attr(755,root,root) %{_libdir}/libopendbxplus.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libopendbxplus.so.1
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/keywords
%dir %{_libdir}/%{name}
%{_mandir}/man1/odbx-sql.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libopendbx.so
%attr(755,root,root) %{_libdir}/libopendbxplus.so
%{_libdir}/libopendbx.la
%{_libdir}/libopendbxplus.la
%{_includedir}/odbx.h
%{_includedir}/opendbx
%{_pkgconfigdir}/opendbx.pc
%{_pkgconfigdir}/opendbxplus.pc
%{_mandir}/man3/OpenDBX*.3*
%{_mandir}/man3/odbx_*.3*

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libopendbx.a
%{_libdir}/libopendbxplus.a
%endif

%files apidocs
%defattr(644,root,root,755)
%doc doc/html/*

%if %{with ibase}
%files backend-firebird
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/libfirebirdbackend.so*
%endif

%files backend-mssql
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/libmssqlbackend.so*

%files backend-mysql
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/libmysqlbackend.so*

%files backend-odbc
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/libodbcbackend.so*

%if %{with oracle}
%files backend-oracle
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/liboraclebackend.so*
%endif

%files backend-postgres
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/libpgsqlbackend.so*

%files backend-sqlite3
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/libsqlite3backend.so*

%files backend-sqlite
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/libsqlitebackend.so*

%files backend-sybase
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/libsybasebackend.so*
