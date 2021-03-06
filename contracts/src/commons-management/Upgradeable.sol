pragma solidity ^0.4.23;

/**
 * @title Upgradeable
 * @dev Interface for contracts that support a being upgraded.
 */
contract Upgradeable {

	bytes4 public constant ERC165_ID_Upgradeable = bytes4(keccak256(abi.encodePacked("upgrade(address)")));

    /**
     * @dev Performs the necessary steps to upgrade from this contract to the specified new version.
     * @param _successor the address of a contract that replaces this one
     * @return true if successful, false otherwise
     */
    function upgrade(address _successor) public returns (bool success);

}