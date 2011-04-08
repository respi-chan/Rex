%{!?perl_sitelib: %define perl_sitelib %(eval "`%{__perl} -V:sitelib`"; echo $sitelib)}
%{!?perl_sitearch: %define perl_sitearch %(eval "`%{__perl} -V:sitearch`"; echo $sitearch)}
%{!?perl_archlib: %define perl_archlib %(eval "`%{__perl} -V:archlib`"; echo $archlib)}

%define real_name Rex

Summary: Rex is a tool to ease the execution of commands on multiple remote servers.
Name: rex
Version: 0.3.1
Release: 1
License: Artistic
Group: Utilities/System
Source: https://github.com/downloads/krimdomu/Rex/Rex-0.3.1.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl-Net-SSH2
BuildRequires: perl >= 5.6.0
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl-Net-SSH2
Requires: perl >= 5.8.0

%description
Rex is a tool to ease the execution of commands on multiple remote 
servers. You can define small tasks, chain tasks to batches, link 
them with servers or server groups, and execute them easily in 
your terminal.

%prep
%setup -n %{real_name}-%{version}
perl Makefile.PL

%build
make 

%install
%{__rm} -rf %{buildroot}
make DESTDIR=%{buildroot} install 

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;


%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root, 0755)
%{_bindir}/*
%{_mandir}/*
%{perl_sitearch}/*
%{perl_sitelib}/*
%{perl_archlib}/*

%changelog
* Thu Mar 31 2011 Jan Gehring <jan.gehring at, gmail.com> 0.3.1-1
- initial rpm

