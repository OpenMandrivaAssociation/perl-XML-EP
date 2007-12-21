%define module 	XML-EP
%define version 0.01
%define release %mkrel 10

Summary:	%{module} perl module
Name: 		perl-%{module}
Version: 	%{version}
Release: 	%{release}
License: 	GPL or Artistic
Group:		Development/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/XML/%{module}-%{version}.tar.bz2
BuildRequires:	perl-devel
Requires:	perl-XML-Parser 
Requires:       perl-XML-XSLT 
BuildRoot: 	%{_tmppath}/%{name}-%{version}-buildroot
Url:		http://search.cpan.org/dist/%{module}
Buildarch:	noarch

%description
%{module} attempts to follow the Cocoon ideas and principles, 
but in a Perl environment.

%prep
%setup -q  -n %{module}-%{version}

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
