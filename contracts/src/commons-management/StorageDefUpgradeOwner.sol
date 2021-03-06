pragma solidity ^0.4.23;

/**
 * @dev Provides the storage layout for database-owning contracts.
 */
contract StorageDefUpgradeOwner {

    address internal upgradeOwner;

    /**
     * @dev Internal constructor to enforce abstract contract.
     */
    constructor() internal {}
}