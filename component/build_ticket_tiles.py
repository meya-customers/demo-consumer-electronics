from dataclasses import dataclass
from meya.button.spec import ButtonElementSpec
from meya.component.element import Component
from meya.component.element import ComponentResponse
from meya.element.field import element_field
from meya.entry import Entry
from meya.tile.spec import TileElementSpec
from meya.zendesk.support.payload.ticket import ZendeskSupportTicketGet
from typing import List


@dataclass
class BuildTicketTilesComponent(Component):
    tickets: List[ZendeskSupportTicketGet] = element_field()

    async def start(self) -> List[Entry]:
        tiles = []
        for ticket in self.tickets:
            tiles.append(
                TileElementSpec(
                    title=f"Ticket {ticket.id} ({ticket.status.value})",
                    description=f"{ticket.subject}",
                    buttons=[
                        ButtonElementSpec(
                            text="View Ticket",
                            url=f"http://example.org/{ticket.id}",
                        )
                    ],
                )
            )
        return self.respond(data=ComponentResponse(tiles))
