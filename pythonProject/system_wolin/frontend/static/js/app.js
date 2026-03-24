// 全局变量
const API_BASE_URL = '';
let studentsData = [];

// 页面加载完成后初始化
document.addEventListener('DOMContentLoaded', function() {
    loadStudents();
    
    // 表单提交事件
    document.getElementById('studentForm').addEventListener('submit', function(e) {
        e.preventDefault();
        saveStudent();
    });
});

// 加载学生列表
async function loadStudents() {
    try {
        showLoading();
        const response = await fetch('/student/get_stu_salary?stu_id=1');
        const result = await response.json();
        
        if (result.code === 200) {
            // 由于API限制，这里我们只能展示一个学生的信息作为示例
            // 实际应用中应该有一个获取所有学生的API
            showMessage('学生信息加载成功', 'success');
            
            // 演示数据（实际应该从后端获取）
            const demoStudents = [
                {
                    id: 1,
                    name: '张三',
                    age: 22,
                    gender: '男',
                    address: '北京市朝阳区',
                    academic: '本科',
                    school: '清华大学',
                    major: '计算机科学与技术',
                    class_id: 1,
                    counselor_id: 1001
                },
                {
                    id: 2,
                    name: '李四',
                    age: 21,
                    gender: '女',
                    address: '上海市浦东新区',
                    academic: '本科',
                    school: '复旦大学',
                    major: '软件工程',
                    class_id: 2,
                    counselor_id: 1002
                },
                {
                    id: 3,
                    name: '王五',
                    age: 23,
                    gender: '男',
                    address: '广州市天河区',
                    academic: '研究生',
                    school: '中山大学',
                    major: '人工智能',
                    class_id: 3,
                    counselor_id: 1003
                }
            ];
            
            studentsData = demoStudents;
            renderStudentTable(studentsData);
        } else {
            showMessage('加载失败：' + result.message, 'error');
        }
    } catch (error) {
        console.error('加载学生列表失败:', error);
        showMessage('网络错误，请稍后重试', 'error');
        
        // 加载失败时显示演示数据
        const demoStudents = [
            {
                id: 1,
                name: '张三',
                age: 22,
                gender: '男',
                address: '北京市朝阳区',
                academic: '本科',
                school: '清华大学',
                major: '计算机科学与技术',
                class_id: 1,
                counselor_id: 1001
            },
            {
                id: 2,
                name: '李四',
                age: 21,
                gender: '女',
                address: '上海市浦东新区',
                academic: '本科',
                school: '复旦大学',
                major: '软件工程',
                class_id: 2,
                counselor_id: 1002
            },
            {
                id: 3,
                name: '王五',
                age: 23,
                gender: '男',
                address: '广州市天河区',
                academic: '研究生',
                school: '中山大学',
                major: '人工智能',
                class_id: 3,
                counselor_id: 1003
            }
        ];
        
        studentsData = demoStudents;
        renderStudentTable(studentsData);
    } finally {
        hideLoading();
    }
}

// 渲染学生表格
function renderStudentTable(students) {
    const tbody = document.getElementById('studentTableBody');
    tbody.innerHTML = '';
    
    if (students.length === 0) {
        tbody.innerHTML = '<tr><td colspan="10" style="text-align: center;">暂无数据</td></tr>';
        return;
    }
    
    students.forEach(student => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${student.id}</td>
            <td>${student.name}</td>
            <td>${student.age}</td>
            <td>${student.gender}</td>
            <td>${student.address}</td>
            <td>${student.academic}</td>
            <td>${student.school}</td>
            <td>${student.major}</td>
            <td>${student.class_id}</td>
            <td>
                <button class="btn btn-info" onclick="editStudent(${student.id})">编辑</button>
                <button class="btn btn-danger" onclick="deleteStudent(${student.id})">删除</button>
            </td>
        `;
        tbody.appendChild(row);
    });
}

// 显示添加学生模态框
function showAddStudentModal() {
    document.getElementById('modalTitle').textContent = '添加学生';
    document.getElementById('studentForm').reset();
    document.getElementById('studentModal').style.display = 'block';
}

// 显示编辑学生模态框
function editStudent(id) {
    const student = studentsData.find(s => s.id === id);
    if (student) {
        document.getElementById('modalTitle').textContent = '编辑学生';
        document.getElementById('studentId').value = student.id;
        document.getElementById('studentId').disabled = true;
        document.getElementById('studentName').value = student.name;
        document.getElementById('studentAge').value = student.age;
        document.getElementById('studentGender').value = student.gender;
        document.getElementById('studentAddress').value = student.address;
        document.getElementById('studentAcademic').value = student.academic;
        document.getElementById('studentSchool').value = student.school;
        document.getElementById('studentMajor').value = student.major;
        document.getElementById('studentClassId').value = student.class_id;
        document.getElementById('studentCounselorId').value = student.counselor_id;
        document.getElementById('studentModal').style.display = 'block';
    } else {
        showMessage('未找到该学生信息', 'error');
    }
}

// 关闭模态框
function closeModal() {
    document.getElementById('studentModal').style.display = 'none';
    document.getElementById('studentForm').reset();
    document.getElementById('studentId').disabled = false;
}

// 保存学生信息
async function saveStudent() {
    const formData = new FormData(document.getElementById('studentForm'));
    const studentData = {
        id: parseInt(formData.get('id')),
        name: formData.get('name'),
        age: parseInt(formData.get('age')),
        gender: formData.get('gender'),
        address: formData.get('address'),
        academic: formData.get('academic'),
        school: formData.get('school'),
        major: formData.get('major'),
        class_id: parseInt(formData.get('class_id')),
        counselor_id: parseInt(formData.get('counselor_id')),
        graduation_time: formData.get('graduation_time'),
        enrollment_time: formData.get('enrollment_time')
    };
    
    try {
        showLoading();
        const response = await fetch('/student/add_student', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(studentData)
        });
        
        const result = await response.json();
        
        if (result.code === 200) {
            showMessage(result.message, 'success');
            closeModal();
            
            // 更新本地数据
            const index = studentsData.findIndex(s => s.id === studentData.id);
            if (index !== -1) {
                // 更新现有学生
                studentsData[index] = studentData;
            } else {
                // 添加新学生
                studentsData.push(studentData);
            }
            
            renderStudentTable(studentsData);
        } else {
            showMessage('操作失败：' + result.message, 'error');
        }
    } catch (error) {
        console.error('保存学生信息失败:', error);
        showMessage('网络错误，请稍后重试', 'error');
    } finally {
        hideLoading();
    }
}

// 删除学生
async function deleteStudent(id) {
    if (!confirm('确定要删除该学生吗？')) {
        return;
    }
    
    try {
        showLoading();
        // 由于没有删除API，这里只是演示
        // 实际应该调用删除API
        
        // 从本地数据中删除
        const index = studentsData.findIndex(s => s.id === id);
        if (index !== -1) {
            studentsData.splice(index, 1);
            renderStudentTable(studentsData);
            showMessage('删除成功', 'success');
        } else {
            showMessage('未找到该学生信息', 'error');
        }
    } catch (error) {
        console.error('删除学生失败:', error);
        showMessage('网络错误，请稍后重试', 'error');
    } finally {
        hideLoading();
    }
}

// 显示消息提示
function showMessage(message, type = 'info') {
    const toast = document.getElementById('messageToast');
    toast.textContent = message;
    toast.className = 'toast ' + type;
    toast.style.display = 'block';
    
    setTimeout(() => {
        toast.style.display = 'none';
    }, 3000);
}

// 显示加载中
function showLoading() {
    // 可以添加加载动画
    console.log('加载中...');
}

// 隐藏加载中
function hideLoading() {
    console.log('加载完成');
}

// 点击模态框外部关闭
window.onclick = function(event) {
    const modal = document.getElementById('studentModal');
    if (event.target === modal) {
        closeModal();
    }
};
