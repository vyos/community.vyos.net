# VyOS Project

VyOS is a fully open-source network OS.

## Goals

* Provide a universal network OS that can run on commodity hardware (from large rack-mountable servers to small desktop appliances and old PCs), all popular hypervisors and cloud platforms.
* Give all people control over their network equipment by giving them the full source code and means to build it.

## History

Back in the days, there was a company named Vyatta inc. that set out to create an open-source network OS
to allow people to replace expensive proprietary routers with free software and commodity hardware.

Indeed, at the time lower-end routers often _were_ commodity hardware already, with proprietary software
intentionally locked into it.  The only big thing missing was a network OS with a unified configuration management system
that could provide the same user experience and reliability as proprietary systems.

Most open-source network OSes focused on SOHO routers and firewalls rather than enterprise and telecom gear,
and these are different domains.
Vyatta created a new approach to building network OS CLIs and managing system upgrades.

Unfortunately, Vyatta inc. hasn't seen an economic success as an independent company (the reasons are beyond the scope
of this discussions). It first started making the software increasingly proprietary, then got acquired by Brocade
and silently discontinued the open-source version altogether.

That would have left the community without a fully open-source network OS suitable for enterprise routers.
Thus, in 2013 a group of long-time Vyatta fans forked the last available code and started a new project
to rescue Vyatta Core and keep it available. That project was named VyOS.

## Team
