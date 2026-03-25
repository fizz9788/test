// 全局变量
let currentResult = null;
let queryHistory = JSON.parse(localStorage.getItem('queryHistory') || '[]');

// 页面加载时初始化
document.addEventListener('DOMContentLoaded', function() {
    renderHistory();
});

// 快捷查询
function quickQuery(question) {
    document.getElementById('queryInput').value = question;
    executeQuery();
}

// 执行查询
async function executeQuery() {
    const question = document.getElementById('queryInput').value.trim();

    if (!question) {
        showToast('请输入查询问题');
        return;
    }

    const queryBtn = document.getElementById('queryBtn');
    const resultSection = document.getElementById('resultSection');
    const loadingIndicator = document.getElementById('loadingIndicator');
    const resultContent = document.getElementById('resultContent');

    // 显示加载状态
    queryBtn.disabled = true;
    resultSection.classList.add('active');
    loadingIndicator.style.display = 'block';
    resultContent.style.display = 'none';

    try {
        console.log('开始查询:', question);
        console.log('请求 URL:', '/ai/text2sql');

        const response = await fetch('/ai/text2sql', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ question: question })
        });

        console.log('响应状态:', response.status);
        console.log('响应 OK:', response.ok);

        if (!response.ok) {
            const errorText = await response.text();
            console.error('响应错误:', errorText);
            throw new Error(`HTTP ${response.status}: ${errorText}`);
        }

        const data = await response.json();
        console.log('响应数据:', data);

        if (data.code === 200 && data.data) {
            currentResult = data.data;

            // 显示 SQL
            document.getElementById('sqlDisplay').textContent =
                'SELECT 语句：' + data.data.sql;

            // 显示结果数量
            document.getElementById('resultCount').textContent =
                '查询到 ' + data.data.count + ' 条结果';

            // 渲染结果表格
            renderResultTable(data.data.result);

            // 显示结果内容
            loadingIndicator.style.display = 'none';
            resultContent.style.display = 'block';

            // 保存到历史记录
            saveToHistory(question);

            showToast('查询成功');
        } else {
            console.error('响应码或数据异常:', data);
            throw new Error(data.message || '查询失败');
        }
    } catch (error) {
        console.error('查询失败:', error);
        console.error('错误堆栈:', error.stack);
        loadingIndicator.style.display = 'none';
        document.getElementById('resultCount').textContent =
            '查询失败：' + error.message;
        resultContent.style.display = 'block';
        document.getElementById('resultTableHead').innerHTML = '';
        document.getElementById('resultTableBody').innerHTML = '';
        showToast('查询失败：' + error.message);
    } finally {
        queryBtn.disabled = false;
    }
}

// 渲染结果表格
function renderResultTable(data) {
    const tableHead = document.getElementById('resultTableHead');
    const tableBody = document.getElementById('resultTableBody');
    
    if (!data || data.length === 0) {
        tableHead.innerHTML = '';
        tableBody.innerHTML = '<tr><td colspan="100%" style="text-align:center;">暂无数据</td></tr>';
        return;
    }

    // 获取表头
    const columns = Object.keys(data[0]);
    
    // 渲染表头
    tableHead.innerHTML = `
        <tr>
            ${columns.map(col => `<th>${col}</th>`).join('')}
        </tr>
    `;
    
    // 渲染表格内容
    tableBody.innerHTML = data.map(row => `
        <tr>
            ${columns.map(col => `<td>${row[col] || '-'}</td>`).join('')}
        </tr>
    `).join('');
}

// 保存到历史记录
function saveToHistory(question) {
    const historyItem = {
        question: question,
        time: new Date().toLocaleString()
    };
    
    queryHistory.unshift(historyItem);
    
    // 只保留最近 20 条记录
    if (queryHistory.length > 20) {
        queryHistory = queryHistory.slice(0, 20);
    }
    
    localStorage.setItem('queryHistory', JSON.stringify(queryHistory));
    renderHistory();
}

// 渲染历史记录
function renderHistory() {
    const historyList = document.getElementById('historyList');

    if (queryHistory.length === 0) {
        historyList.innerHTML = '<li style="color:#999; text-align:center; padding:20px;">暂无查询历史</li>';
        return;
    }

    historyList.innerHTML = queryHistory.map(item => {
        const escapedQuestion = item.question.replace(/'/g, "\\'");
        return `
        <li class="history-item" onclick="quickQuery('${escapedQuestion}')">
            <div class="history-question">${item.question}</div>
            <div class="history-time">${item.time}</div>
        </li>
        `;
    }).join('');
}

// 导出为 CSV
function exportToCSV() {
    if (!currentResult || !currentResult.result || currentResult.result.length === 0) {
        showToast('没有可导出的数据');
        return;
    }

    const data = currentResult.result;
    const columns = Object.keys(data[0]);

    // 构建 CSV 内容
    let csvContent = columns.join(',') + '\n';

    data.forEach(row => {
        const rowStr = columns.map(col => {
            const value = row[col] || '';
            const valueStr = String(value);
            // 处理包含逗号或引号的字段
            if (valueStr.includes(',') || valueStr.includes('"')) {
                return '"' + valueStr.replace(/"/g, '""') + '"';
            }
            return valueStr;
        }).join(',');
        csvContent += rowStr + '\n';
    });

    // 创建下载链接
    const blob = new Blob(['\ufeff' + csvContent], { type: 'text/csv;charset=utf-8;' });
    const link = document.createElement('a');
    const url = URL.createObjectURL(blob);

    link.setAttribute('href', url);
    link.setAttribute('download', '查询结果_' + new Date().getTime() + '.csv');
    link.style.visibility = 'hidden';

    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);

    showToast('导出成功');
}

// 显示提示消息
function showToast(message) {
    const toast = document.getElementById('messageToast');
    toast.textContent = message;
    toast.style.display = 'block';
    toast.style.opacity = '1';
    
    setTimeout(() => {
        toast.style.opacity = '0';
        setTimeout(() => {
            toast.style.display = 'none';
        }, 300);
    }, 3000);
}
