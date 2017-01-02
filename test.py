def hasEmployee(manager, employee):
    if manager.get_id() == employee.get_id():
        return True
    for direct_employee in manager.get_reports():
        if direct_employee.get_id() == employee.get_id():
            return True
    for direct_employee in manager.get_reports():
        if hasEmployee(direct_employee, employee):
            return True
    return False

# RETURN "None" IF THERE IS NO CLOSEST COMMON MANAGER
# OR THE GIVEN EMPLOYEES ARE NOT THE PART OF THE COMPANY
def closestCommonManagerRec(ceo, employee1, employee2):
    # WRITE YOUR CODE HERE
 #   if not hasEmployee(ceo, employee1) or not hasEmployee(ceo, employee2):
 #       return None
    if ceo.get_id() == employee1.get_id():
        if hasEmployee(ceo, employee2):
            return (0, ceo)
        else
            return (1, None)
    if ceo.get_id() == employee2.get_id():
        if hasEmployee(ceo, employee1):
            return (0, ceo)
        else
            return (2, None)
    employee1_found = False
    employee2_found = False
    for direct_employee in ceo.get_reports():
        (res, manager) = closestCommonManager(direct_employee, employee1, employee2)
        if res == 0:
            if (manager):
                return (0, manager)
        elif res == 1:
            employee1_found = True
        else:
            employee2_found = True
    if (employee1_found and employee2_found):
        return (0, ceo)
    else:
        return (0, None)
