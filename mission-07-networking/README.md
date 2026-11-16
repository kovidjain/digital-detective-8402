# Mission 7 — How computers communicate

## Mission title

How computers communicate.

## Task / objective

I needed to explain how computers communicate across networks, including the roles of clients, servers, routers, DNS, and common protocols. I also needed to follow a simple request from an application to a remote service.

## Work completed

- Explained the difference between a client and a server.
- Described how routers move packets between networks.
- Explained how DNS maps names to network addresses.
- Compared common protocols and their purposes.
- Traced a simplified request from a browser to a web server and back.
- Kept examples general without personal addresses, account details, or private network information.

## Commands / tools used

- Markdown — wrote the networking explanations and tables.
- Git — tracked the Mission 7 changes.
- GitHub — stored and reviewed the completed mission.

## My understanding

Networking works because different devices follow shared rules. A client requests a service, a server responds, DNS helps find the server's address, routers forward packets, and protocols define how the messages are structured and exchanged. Each layer has a focused job, which makes communication between different systems possible.

## Difficulties faced

It was easy to treat DNS as if it carried the whole web request or to treat a router as if it understood the application content. In reality, these components have different responsibilities.

## How I resolved them

I separated name lookup, packet forwarding, reliable transport, and application messages into distinct steps. I then used one web request to show how the parts fit together without claiming that the network path is always identical.

## Evidence / files

- [`networking-notes.md`](networking-notes.md) — DNS, routers, protocols, client-server roles, and request flow.

## Commit details

Commit message: `Explain computer networking fundamentals`

Only Mission 7 files are included in this mission commit.
