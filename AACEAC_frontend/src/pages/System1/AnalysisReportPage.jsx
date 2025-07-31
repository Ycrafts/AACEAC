import React, { useEffect, useState } from 'react';
import { getWoredas, getOrganizationalUnits, getEmployees } from '../../api';

const AnalysisReportPage = () => {
  const [woredaCount, setWoredaCount] = useState(0);
  const [orgUnitCount, setOrgUnitCount] = useState(0);
  const [activeEmployeesCount, setActiveEmployeesCount] = useState(0);
  const [resignedEmployeesCount, setResignedEmployeesCount] = useState(0);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchCounts = async () => {
      setLoading(true);
      setError(null);
      try {
        // Fetch woredas and organizational units for counts
        const [woredaRes, orgUnitRes] = await Promise.all([
          getWoredas(1, 1),
          getOrganizationalUnits(1, 1)
        ]);
        setWoredaCount(woredaRes.data.count);
        setOrgUnitCount(orgUnitRes.data.count);

        // Fetch all employees to count by status
        const employeesRes = await getEmployees(1, 1000); // Get a large number to fetch all employees
        const employees = employeesRes.data.results || employeesRes.data;
        
        // Count active and resigned employees
        const activeCount = employees.filter(emp => emp.status === "Active").length;
        const resignedCount = employees.filter(emp => emp.status === "Resigned").length;
        
        setActiveEmployeesCount(activeCount);
        setResignedEmployeesCount(resignedCount);
      } catch (err) {
        setError('Failed to fetch counts.');
        setWoredaCount(0);
        setOrgUnitCount(0);
        setActiveEmployeesCount(0);
        setResignedEmployeesCount(0);
      } finally {
        setLoading(false);
      }
    };
    fetchCounts();
  }, []);

  return (
    <div className="container mx-auto px-4 py-8">
      <div className="bg-slate-100 dark:bg-slate-800 rounded-lg shadow p-8">
        <h2 className="text-2xl font-bold mb-6">Analysis Report</h2>
        {loading ? (
          <p>Loading...</p>
        ) : error ? (
          <p className="text-red-500">{error}</p>
        ) : (
          <table className="min-w-full text-left border border-slate-200 dark:border-slate-700 rounded-lg overflow-hidden">
            <thead className="bg-slate-50 dark:bg-slate-800">
              <tr>
                <th className="px-6 py-3 text-slate-700 dark:text-slate-200 font-semibold">Name</th>
                <th className="px-6 py-3 text-slate-700 dark:text-slate-200 font-semibold">Total</th>
              </tr>
            </thead>
            <tbody className="bg-white dark:bg-slate-900">
              <tr>
                <td className="px-6 py-4 font-medium">Woredas</td>
                <td className="px-6 py-4">{woredaCount}</td>
              </tr>
              <tr>
                <td className="px-6 py-4 font-medium">Organizational Units</td>
                <td className="px-6 py-4">{orgUnitCount}</td>
              </tr>
              <tr>
                <td className="px-6 py-4 font-medium">Active Employees</td>
                <td className="px-6 py-4">{activeEmployeesCount}</td>
              </tr>
              <tr>
                <td className="px-6 py-4 font-medium">Resigned Employees</td>
                <td className="px-6 py-4">{resignedEmployeesCount}</td>
              </tr>
            </tbody>
          </table>
        )}
      </div>
    </div>
  );
};

export default AnalysisReportPage;
