#
# Conditional build:
%bcond_without  tests           # do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Module
%define	pnam	Versions-Report
Summary:	Module::Versions::Report -- report versions of all modules in memory
#Summary(pl):	
Name:		perl-Module-Versions-Report
Version:	1.02
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a2ef9353386df4c4e49c7e4031c45bd3
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
I often get email from someone reporting a bug in a module I've written.
I email back, asking what version of the module it is, what version of
Perl on what OS, and sometimes what version of some relevent third library
(like XML::Parser).  They reply, saying "Perl 5".  I say "I need the exact
version, as reported by C<perl -v>".  They tell me.  And I say "I, uh,
also asked about the version of my module and XML::Parser [or whatever]".
They say "Oh yeah.  It's 2.27".  "Is that my module or XML::Parser?"
"XML::Parser."  "OK, and what about my module's version?"  "Ohyeah.
That's 3.11."  By this time, days have passed, and what should have been
a simple operation -- reporting the version of Perl and relevent modules,
has been needlessly complicated.

This module is for simplifying that task.  If you add "use
Module::Versions::Report;" to a program (especially handy if your program
is one that demonstrates a bug in some module), then when the program
has finished running, you well get a report detailing the all modules
in memory, and noting the version of each (for modules that defined a
C<$VERSION>, at least).

# %description -l pl
# TODO

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
%{perl_vendorlib}/Module/Versions/*.pm
%{_mandir}/man3/*
