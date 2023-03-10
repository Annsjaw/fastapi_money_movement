from typing import List, Optional
from sqlalchemy.orm import Session
from fastapi import Depends
from ..database import get_session
from .. import tables
from ..models.operations import Operation, OperationKind


class OperationService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def get_list(self, kind: Optional[OperationKind] = None) -> List[tables.Operation]:
        query = self.session.query(tables.Operation)
        if kind:
            query = query.filter_by(kind=kind)
        operations = query.all()
        return operations
