%define upstream_name 	 XML-EP
%define upstream_version 0.01

Name: 		perl-%{upstream_name}
Version: 	%perl_convert_version %{upstream_version}
Release: 	%mkrel 1

Summary:	%{upstream_name} perl module
License: 	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/XML/%{upstream_name}-%{upstream_version}.tar.bz2

Requires:	perl-XML-Parser 
Requires:   perl-XML-XSLT 
Buildarch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
%{upstream_name} attempts to follow the Cocoon ideas and principles, 
but in a Perl environment.

%prep
%setup -q  -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean 
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(-,root,root)
%doc ChangeLog README MANIFEST examples
%_bindir/*
%{perl_vendorlib}/XML/*.pm
%{perl_vendorlib}/XML/EP/*
%{_mandir}/*/*
