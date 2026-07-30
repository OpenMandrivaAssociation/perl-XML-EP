%define upstream_name 	 XML-EP
%define upstream_version 0.01
Name:		perl-%{upstream_name}
Version:	0.01
Release:	2

Summary:	%{upstream_name} perl module
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/XML-EP
Source0:	https://cpan.metacpan.org/authors/id/J/JW/JWIED/XML-EP-0.01.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
Requires:	perl(XML::Parser)
Requires:	perl(XML::XSLT)
BuildArch:	noarch

%description
%{upstream_name} attempts to follow the Cocoon ideas and principles, 
but in a Perl environment.

%prep
%setup -q  -n XML-EP-0.01

%build
perl Makefile.PL INSTALLDIRS=vendor
make

%install
%makeinstall_std

%files 
%doc ChangeLog README MANIFEST examples
%{_bindir}/*
%{perl_vendorlib}/XML/*.pm
%{perl_vendorlib}/XML/EP/*
%{_mandir}/*/*

