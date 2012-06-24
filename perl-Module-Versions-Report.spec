#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Module
%define		pnam	Versions-Report
Summary:	Module::Versions::Report - report versions of all modules in memory
Summary(pl):	Module::Versions::Report - raportowanie wersji wszystkich modu��w w pami�ci
Name:		perl-Module-Versions-Report
Version:	1.02
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a2ef9353386df4c4e49c7e4031c45bd3
URL:		http://search.cpan.org/dist/Module-Versions-Report
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
I often get email from someone reporting a bug in a module I've written.
I email back, asking what version of the module it is, what version of
Perl on what OS, and sometimes what version of some relevant third library
(like XML::Parser). They reply, saying "Perl 5". I say "I need the exact
version, as reported by `perl -v`". They tell me. And I say "I, uh,
also asked about the version of my module and XML::Parser [or whatever]".
They say "Oh yeah. It's 2.27". "Is that my module or XML::Parser?"
"XML::Parser." "OK, and what about my module's version?" "Ohyeah.
That's 3.11." By this time, days have passed, and what should have been
a simple operation - reporting the version of Perl and relevant modules,
has been needlessly complicated.

This module is for simplifying that task. If you add "use
Module::Versions::Report;" to a program (especially handy if your program
is one that demonstrates a bug in some module), then when the program
has finished running, you well get a report detailing the all modules
in memory, and noting the version of each (for modules that defined a
$VERSION, at least).

%description -l pl
Autor cz�sto dostaje raporty b��d�w w napisanych przez niego modu��w.
Odpisuj�c pyta si� o wersj� modu�u, wersj� Perla, system operacyjny i
czasem wersje powi�zanych bibliotek (np. XML::Parser). W odpowiedzi
cz�sto dostaje "Perl 5", podczas gdy potrzebuje dok�adnej wersji,
takiej jak wypisywana przez `perl -v`". I podobnie dla innych modu��w.
Ca�� ta konwersacja mo�e trwa� wiele dni, a powinna by� prost�
operacj� - raportowaniem wersji Perla i powi�zanych modu��w.

Ten modu� s�u�y do uproszczenia tego zadania. Po dodaniu "use
Module::Versions::Report" do programu (co jest szczeg�lnie por�czne,
je�li program s�u�y do demonstrowania b��du w module), program po
uruchomieniu wypisuje raport ze szczeg�ami na temat wszystkich
modu��w obecnych w pami�ci, podaj�c ich wersje (przynajmniej dla
modu��w definiuj�cych $VERSION).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog
%dir %{perl_vendorlib}/Module/Versions
%{perl_vendorlib}/Module/Versions/*.pm
%{_mandir}/man3/*
