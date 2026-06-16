# Memory Scanner MCP

基于 [pymem](https://github.com/srounet/Pymem) 的内存扫描与修改 MCP 服务器。

通过 MCP 协议将内存读写、扫描、特征码搜索等能力暴露给 AI Agent，实现自然语言驱动的内存修改。

## 功能

| 工具 | 说明 |
|------|------|
| `list_processes` | 列出运行中的进程 |
| `attach_process` | 附加到目标进程 |
| `detach_process` | 断开进程连接 |
| `get_process_info` | 获取进程详细信息和模块列表 |
| `read_memory` | 读取指定地址的值 |
| `write_memory` | 写入值到指定地址 |
| `scan_memory_first` | 首次扫描（全内存搜索） |
| `scan_memory_next` | 再次扫描（缩小范围） |
| `scan_memory_filter` | 条件过滤（大于/小于等） |
| `write_scan_results` | 批量写入扫描结果 |
| `get_scan_results` | 查看扫描结果及当前值 |
| `scan_pattern` | AOB/特征码扫描（支持通配符） |
| `get_module_base` | 获取模块基地址 |
| `read_pointer_chain` | 多级指针链读取 |
| `write_pointer_chain` | 多级指针链写入 |
| `dump_memory` | 内存转储（Hex + ASCII） |
| `freeze_address` | 冻结地址值 |
| `unfreeze_address` | 解除冻结 |
| `apply_frozen` | 执行冻结写入 |
| `list_frozen` | 列出冻结列表 |

## 支持的数据类型

`int8` `int16` `int32` `int64` `uint8` `uint16` `uint32` `uint64` `float` `double` `string` `bytes`

## 安装

### 从源码安装（推荐开发使用）

```bash
git clone https://github.com/miloira/MemoryScaner.git
cd MemoryScaner
pip install -e .
```

### 直接安装

```bash
pip install memory-scanner-mcp
```

> 需要 Python 3.10+，仅支持 Windows。

## 使用方式

### 作为命令行工具运行

```bash
memory-scanner-mcp
```

### 作为 Python 模块运行

```bash
python -m memory_scanner
```

### MCP 客户端配置

推荐使用 `uvx`（无需手动安装）：

```json
{
  "mcpServers": {
    "memory-scanner": {
      "command": "uvx",
      "args": ["memory-scanner-mcp"]
    }
  }
}
```

也可以先 `pip install` 后直接使用命令：

```json
{
  "mcpServers": {
    "memory-scanner": {
      "command": "memory-scanner-mcp"
    }
  }
}
```

或者使用 Python 模块方式：

```json
{
  "mcpServers": {
    "memory-scanner": {
      "command": "python",
      "args": ["-m", "memory_scanner"]
    }
  }
}
```

## 项目结构

```
MemoryScaner/
├── pyproject.toml          # 项目配置与依赖管理
├── README.md
├── LICENSE
└── src/
    └── memory_scanner/
        ├── __init__.py     # 包初始化与版本号
        ├── __main__.py     # python -m memory_scanner 入口
        └── server.py       # MCP 服务器实现（所有工具定义）
```

## 使用示例

典型的内存修改流程（以游戏修改为例）：

1. **附加进程**: "附加到 game.exe"
2. **首次扫描**: "搜索 int32 类型的值 100"（当前血量为100）
3. **改变值**: 在游戏中让血量变化
4. **再次扫描**: "搜索新的值 95"（血量变为95）
5. **重复缩小**: 直到结果只剩1-2个
6. **修改值**: "把找到的地址写入 9999"
7. **冻结**: "冻结这个地址为 9999"

## 开发

```bash
# 克隆项目
git clone https://github.com/miloira/MemoryScaner.git
cd MemoryScaner

# 创建虚拟环境
python -m venv .venv
.venv\Scripts\activate

# 安装开发依赖（可编辑模式）
pip install -e .
```

## 注意事项

- 必须以 **管理员权限** 运行才能读写其他进程的内存
- 部分进程有保护机制，可能无法正常读写
- 冻结功能需要客户端定期调用 `apply_frozen` 来维持
- 扫描大量内存时可能需要较长时间

## 许可证

MIT
