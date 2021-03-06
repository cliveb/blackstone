[
  {
    "TableName": "AGREEMENTS",
    "Filter": "Log1Text = 'AN://agreement'",
    "Columns": {
      "agreementAddress": {
        "name": "agreementAddress",
        "type": "address",
        "primary": true
      },
      "archetype": {
        "name": "archetype",
        "type": "address"
      },
      "name": {
        "name": "name",
        "type": "string"
      },
      "creator": {
        "name": "creator",
        "type": "address"
      },
      "isPrivate": {
        "name": "isPrivate",
        "type": "bool"
      },
      "legalState": {
        "name": "legalState",
        "type": "uint8"
      },
      "maxNumberOfEvents": {
        "name": "maxNumberOfEvents",
        "type": "uint32"
      },
      "formationProcessInstance": {
        "name": "formationProcessInstance",
        "type": "address"
      },
      "executionProcessInstance": {
        "name": "executionProcessInstance",
        "type": "address"
      },
      "hoardAddress": {
        "name": "hoardAddress",
        "type": "bytes32"
      },
      "hoardSecret": {
        "name": "hoardSecret",
        "type": "bytes32"
      },
      "eventLogHoardAddress": {
        "name": "eventLogHoardAddress",
        "type": "bytes32"
      },
      "eventLogHoardSecret": {
        "name": "eventLogHoardSecret",
        "type": "bytes32"
      }
    }
  },
  {
    "TableName": "AGREEMENT_COLLECTIONS",
    "Filter": "Log1Text = 'AN://agreement/collection'",
    "Columns": {
      "id": {
        "name": "id",
        "type": "bytes32",
        "primary": true
      },
      "name": {
        "name": "name",
        "type": "string"
      },
      "author": {
        "name": "author",
        "type": "address"
      },
      "collectionType": {
        "name": "collectionType",
        "type": "uint8"
      },
      "packageId": {
        "name": "packageId",
        "type": "bytes32"
      }
    }
  },
  {
    "TableName": "AGREEMENT_TO_PARTY",
    "Filter": "Log1Text = 'AN://agreement-to-party'",
    "Columns": {
      "agreementAddress": {
        "name": "agreementAddress",
        "type": "address",
        "primary": true
      },
      "party": {
        "name": "party",
        "type": "address",
        "primary": true
      }
    }
  },
  {
    "TableName": "AGREEMENT_TO_COLLECTION",
    "Filter": "Log1Text = 'AN://agreement-to-collection'",
    "Columns": {
      "collectionId": {
        "name": "collectionId",
        "type": "bytes32",
        "primary": true
      },
      "agreementAddress": {
        "name": "agreementAddress",
        "type": "address",
        "primary": true
      },
      "agreementName": {
        "name": "agreementName",
        "type": "string"
      },
      "archetypeAddress": {
        "name": "archetypeAddress",
        "type": "address"
      }
    }
  },
  {
    "TableName": "ARCHETYPES",
    "Filter": "Log1Text = 'AN://archetype'",
    "Columns": {
      "archetypeAddress": {
        "name": "archetypeAddress",
        "type": "address",
        "primary": true
      },
      "name": {
        "name": "name",
        "type": "string"
      },
      "description": {
        "name": "description",
        "type": "string"
      },
      "price": {
        "name": "price",
        "type": "uint32"
      },
      "author": {
        "name": "author",
        "type": "address"
      },
      "active": {
        "name": "active",
        "type": "bool"
      },
      "isPrivate": {
        "name": "isPrivate",
        "type": "bool"
      },
      "successor": {
        "name": "successor",
        "type": "address"
      },
      "formationProcessDefinition": {
        "name": "formationProcessDefinition",
        "type": "address"
      },
      "executionProcessDefinition": {
        "name": "executionProcessDefinition",
        "type": "address"
      }
    }
  },
  {
    "TableName": "ARCHETYPE_PACKAGES",
    "Filter": "Log1Text = 'AN://archetype/package'",
    "Columns": {
      "id": {
        "name": "id",
        "type": "bytes32",
        "primary": true
      },
      "name": {
        "name": "name",
        "type": "string"
      },
      "description": {
        "name": "description",
        "type": "string"
      },
      "author": {
        "name": "author",
        "type": "address"
      },
      "isPrivate": {
        "name": "isPrivate",
        "type": "bool"
      },
      "active": {
        "name": "active",
        "type": "bool"
      }
    }
  },
  {
    "TableName": "ARCHETYPE_TO_PACKAGE",
    "Filter": "Log1Text = 'AN://archetype-to-package'",
    "Columns": {
      "packageId": {
        "name": "packageId",
        "type": "bytes32",
        "primary": true
      },
      "archetypeAddress": {
        "name": "archetypeAddress",
        "type": "address",
        "primary": true
      },
      "archetypeName": {
        "name": "archetypeName",
        "type": "string"
      }
    }
  },
  {
    "TableName": "ARCHETYPE_PARAMETERS",
    "Filter": "Log1Text = 'AN://archetype/parameter'",
    "Columns": {
      "archetypeAddress": {
        "name": "archetypeAddress",
        "type": "address",
        "primary": true
      },
      "parameterName": {
        "name": "parameterName",
        "type": "bytes32",
        "primary": true
      },
      "parameterType": {
        "name": "parameterType",
        "type": "uint8"
      },
      "position": {
        "name": "position",
        "type": "uint256"
      }
    }
  },
  {
    "TableName": "ARCHETYPE_DOCUMENTS",
    "Filter": "Log1Text = 'AN://archetype/document'",
    "Columns": {
      "archetypeAddress": {
        "name": "archetypeAddress",
        "type": "address",
        "primary": true
      },
      "documentKey": {
        "name": "documentKey",
        "type": "bytes32",
        "primary": true
      },
      "hoardAddress": {
        "name": "hoardAddress",
        "type": "bytes32"
      },
      "secretKey": {
        "name": "secretKey",
        "type": "bytes32"
      }
    }
  },
  {
    "TableName": "ARCHETYPE_JURISDICTIONS",
    "Filter": "Log1Text = 'AN://archetype/jurisdiction'",
    "Columns": {
      "archetypeAddress": {
        "name": "archetypeAddress",
        "type": "address",
        "primary": true
      },
      "country": {
        "name": "country",
        "type": "bytes2",
        "primary": true,
        "bytesToString": true
      },
      "region": {
        "name": "region",
        "type": "bytes32",
        "primary": true
      }
    }
  },
  {
    "TableName": "GOVERNING_ARCHETYPES",
    "Filter": "Log1Text = 'AN://governing-archetype'",
    "Columns": {
      "archetypeAddress": {
        "name": "archetypeAddress",
        "type": "address",
        "primary": true
      },
      "governingArchetypeAddress": {
        "name": "governingArchetypeAddress",
        "type": "address",
        "primary": true
      },
      "governingArchetypeName": {
        "name": "governingArchetypeName",
        "type": "string"
      }
    }
  },
  {
    "TableName": "ACTIVITY_INSTANCES",
    "Filter": "Log1Text = 'AN://activity/instance'",
    "Columns": {
      "activityInstanceId": {
        "name": "activityInstanceId",
        "type": "bytes32",
        "primary": true
      },
      "activityId": {
        "name": "activityId",
        "type": "bytes32",
        "bytesToString": true
      },
      "processInstance": {
        "name": "processInstance",
        "type": "address"
      },
      "created": {
        "name": "created",
        "type": "uint"
      },
      "completed": {
        "name": "completed",
        "type": "uint"
      },
      "performer": {
        "name": "performer",
        "type": "address"
      },
      "completedBy": {
        "name": "completedBy",
        "type": "address"
      },
      "state": {
        "name": "state",
        "type": "uint8"
      }
    }
  },
  {
    "TableName": "PROCESS_INSTANCES",
    "Filter": "Log1Text = 'AN://process/instance'",
    "Columns": {
      "processAddress": {
        "name": "processAddress",
        "type": "address",
        "primary": true
      },
      "processDefinition": {
        "name": "processDefinition",
        "type": "address"
      },
      "state": {
        "name": "state",
        "type": "uint8"
      },
      "startedBy": {
        "name": "startedBy",
        "type": "address"
      }
    }
  },
  {
    "TableName": "ACTIVITY_DEFINITIONS",
    "Filter": "Log1Text = 'AN://activity/definition'",
    "Columns": {
      "activityDefinitionId": {
        "name": "activityDefinitionId",
        "type": "bytes32",
        "primary": true,
        "bytesToString": true
      },
      "modelAddress": {
        "name": "modelAddress",
        "type": "address"
      },
      "processDefinitionAddress": {
        "name": "processDefinitionAddress",
        "type": "address"
      },
      "activityType": {
        "name": "activityType",
        "type": "uint8"
      },
      "taskType": {
        "name": "taskType",
        "type": "uint8"
      },
      "taskBehavior": {
        "name": "taskBehavior",
        "type": "uint8"
      },
      "assignee": {
        "name": "assignee",
        "type": "bytes32",
        "bytesToString": true
      },
      "multiInstance": {
        "name": "multiInstance",
        "type": "bool"
      },
      "application": {
        "name": "application",
        "type": "bytes32",
        "bytesToString": true
      },
      "subProcessModelId": {
        "name": "subProcessModelId",
        "type": "bytes32",
        "bytesToString": true
      },
      "subProcessDefinitionId": {
        "name": "subProcessDefinitionId",
        "type": "bytes32",
        "bytesToString": true
      }
    }
  },
  {
    "TableName": "PROCESS_DEFINITIONS",
    "Filter": "Log1Text = 'AN://process/definition'",
    "Columns": {
      "processDefinitionAddress": {
        "name": "processDefinitionAddress",
        "type": "address",
        "primary": true
      },
      "id": {
        "name": "id",
        "type": "bytes32",
        "bytesToString": true
      },
      "interfaceId": {
        "name": "interfaceId",
        "type": "bytes32",
        "bytesToString": true
      },
      "modelId": {
        "name": "modelId",
        "type": "bytes32",
        "bytesToString": true
      }
    }
  }
]