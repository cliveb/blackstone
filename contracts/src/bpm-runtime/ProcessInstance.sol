pragma solidity ^0.4.23;

import "commons-base/OwnerTransferable.sol";
import "commons-collections/DataStorage.sol";
import "commons-collections/AddressScopes.sol";

import "bpm-runtime/BpmService.sol";
import "bpm-runtime/ProcessStateChangeEmitter.sol";
import "bpm-runtime/TransitionConditionResolver.sol";

/**
 * @title ProcessInstance Interface
 * @dev Interface for a BPM container that represents a process instance providing a data context for activities and code participating in the process.
 */
contract ProcessInstance is DataStorage, AddressScopes, OwnerTransferable, ProcessStateChangeEmitter, TransitionConditionResolver {

	/**
	 * @dev Initiates and populates the runtime graph that will handle the state of this ProcessInstance.
	 */
	function initRuntime() public;

	/**
	 * @dev Initiates execution of this ProcessInstance consisting of attempting to activate and process any activities and advance the
	 * state of the runtime graph.
	 * @param _service the BpmService managing this ProcessInstance (required for changes to this ProcessInstance and access to the BpmServiceDb)
	 * @return error code indicating success or failure
	 */
	function execute(BpmService _service) public returns (uint error);

	/**
	 * @dev Completes the specified activity
	 * @param _activityInstanceId the activity instance
	 * @param _service the BpmService managing this ProcessInstance (required for changes to this ProcessInstance after the activity completes)
	 * @return an error code indicating success or failure
	 */
	function completeActivity(bytes32 _activityInstanceId, BpmService _service) external returns (uint error);

	/**
	 * @dev Aborts this ProcessInstance and halts any ongoing activities. After the abort the ProcessInstance cannot be resurrected.
     * @param _service the BpmService to emit update events for ActivityInstances
	 */
	function abort(BpmService _service) external;

    /**
     * @dev Resolves the target storage location for the specified IN data mapping in the context of the given activity instance.
     * @param _activityInstanceId the ID of an activity instance
     * @param _dataMappingId the ID of a data mapping defined for the activity
     * @return dataStorage - the address of a DataStorage
     * @return dataPath - the dataPath under which to find data mapping value
     */
    function resolveInDataLocation(bytes32 _activityInstanceId, bytes32 _dataMappingId) public view returns (address dataStorage, bytes32 dataPath);

    /**
     * @dev Resolves the target storage location for the specified OUT data mapping in the context of the given activity instance.
     * @param _activityInstanceId the ID of an activity instance
     * @param _dataMappingId the ID of a data mapping defined for the activity
     * @return dataStorage - the address of a DataStorage
     * @return dataPath - the dataPath under which to find data mapping value
     */
    function resolveOutDataLocation(bytes32 _activityInstanceId, bytes32 _dataMappingId) public view returns (address dataStorage, bytes32 dataPath);

	/**
	 * @dev Returns the process definition on which this instance is based.
	 * @return the address of a ProcessDefinition
	 */
	function getProcessDefinition() external view returns (address);

	/**
	 * @dev Returns the state of this process instance
	 * @return the uint representation of the BpmRuntime.ProcessInstanceState
	 */
	function getState() external view returns (uint8);

    /**
     * @dev Returns the account that started this process instance
     * @return the address registered when creating the process instance
     */
    function getStartedBy() external view returns (address);

	/**
	 * @dev Returns the number of activity instances currently contained in this ProcessInstance.
	 * Note that this number is subject to change as long as the process isntance is not completed.
	 * @return the number of activity instances
	 */
	function getNumberOfActivityInstances() external view returns (uint size);

	/**
	 * @dev Returns the globally unique ID of the activity instance at the specified index in the ProcessInstance.
	 * @param _idx the index position
	 * @return the bytes32 ID
	 */
	function getActivityInstanceAtIndex(uint _idx) external view returns (bytes32);

	/**
	 * @dev Returns information about the activity instance with the specified ID
	 * @param _id the global ID of the activity instance
	 * @return activityId - the ID of the activity as defined by the process definition
	 * @return created - the creation timestamp
	 * @return completed - the completion timestamp
	 * @return performer - the account who is performing the activity (for interactive activities only)
	 * @return completedBy - the account who completed the activity (for interactive activities only) 
	 * @return state - the uint8 representation of the BpmRuntime.ActivityInstanceState of this activity instance
	 */
	function getActivityInstanceData(bytes32 _id) external view returns (bytes32 activityId, uint created, uint completed, address performer, address completedBy, uint8 state);

}